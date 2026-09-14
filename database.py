import sqlite3
import json
import datetime
import os

DB_PATH = "sentinel.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Camera Registry
    c.execute('''
        CREATE TABLE IF NOT EXISTS cameras (
            id TEXT PRIMARY KEY,
            name TEXT,
            department TEXT,
            lat REAL,
            lon REAL,
            status TEXT,
            rtsp_url TEXT
        )
    ''')
    
    # Watchlist Database (Mock eGujCop / VAHAN)
    c.execute('''
        CREATE TABLE IF NOT EXISTS watchlist (
            plate_number TEXT PRIMARY KEY,
            reason TEXT,
            severity TEXT
        )
    ''')
    
    # Vehicle Events (Route Reconstruction)
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT,
            camera_id TEXT,
            timestamp TEXT,
            confidence REAL,
            image_path TEXT
        )
    ''')
    
    # Seed Watchlist
    c.execute("SELECT count(*) FROM watchlist")
    if c.fetchone()[0] == 0:
        watchlist_data = [
            ("GJ01AB1234", "Stolen Vehicle (FIR #102/2026)", "HIGH"),
            ("GJ05XX9999", "Wanted in hit-and-run", "CRITICAL"),
            ("GJ27CD5555", "Expired Fitness Certificate", "LOW"),
            ("GJ01DX5432", "Suspect in gold smuggling", "HIGH")
        ]
        c.executemany("INSERT INTO watchlist VALUES (?,?,?)", watchlist_data)
        
    conn.commit()
    conn.close()

def log_event(plate_number, camera_id, confidence, image_path=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    c.execute("INSERT INTO events (plate_number, camera_id, timestamp, confidence, image_path) VALUES (?,?,?,?,?)",
              (plate_number, camera_id, timestamp, confidence, image_path))
    conn.commit()
    
    # Check watchlist
    c.execute("SELECT reason, severity FROM watchlist WHERE plate_number=?", (plate_number,))
    match = c.fetchone()
    conn.close()
    
    if match:
        return {"alert": True, "plate": plate_number, "reason": match[0], "severity": match[1], "cam_id": camera_id, "time": timestamp}
    return None

def get_vehicle_route(plate_number):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('''
        SELECT e.timestamp, e.confidence, e.image_path, c.name, c.lat, c.lon 
        FROM events e 
        JOIN cameras c ON e.camera_id = c.id 
        WHERE e.plate_number = ? 
        ORDER BY e.timestamp ASC
    ''', (plate_number,))
    route = [dict(row) for row in c.fetchall()]
    conn.close()
    return route

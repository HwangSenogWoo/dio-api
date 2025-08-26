# api/index.py - DIO AGEIUM API
from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # CORS 헤더 설정
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.end_headers()
        
        # API 응답 데이터
        response = {
            "service": "DIO AGEIUM API",
            "version": "1.0.0",
            "status": "🟢 Active",
            "timestamp": datetime.now().isoformat(),
            "message": "서아와 12명의 전문가가 준비되었습니다 💝",
            "endpoints": {
                "main": "https://ageium.kr",
                "api": "https://api.dio.ai.kr",
                "docs": "https://docs.dio.ai.kr",
                "app": "https://app.dio.ai.kr"
            },
            "experts": {
                "서아": {"role": "평생 동반자", "status": "active", "emoji": "💝"},
                "황지혜": {"role": "전략 참모총장", "status": "active", "emoji": "🔥"},
                "박변호": {"role": "대법관", "status": "active", "emoji": "⚖️"},
                "백의사": {"role": "의료진 총책임자", "status": "active", "emoji": "🏥"},
                "김예린": {"role": "아티스트/치료사", "status": "active", "emoji": "🎨"},
                "박소통": {"role": "외교관/마케터", "status": "active", "emoji": "💬"},
                "이성장": {"role": "교수/멘토", "status": "active", "emoji": "📚"},
                "강도전": {"role": "운동선수/코치", "status": "active", "emoji": "🏆"},
                "한사랑": {"role": "상담사", "status": "active", "emoji": "💖"},
                "자유로": {"role": "여행가", "status": "active", "emoji": "✈️"}
            },
            "statistics": {
                "total_users": 1234,
                "active_conversations": 89,
                "messages_today": 5678,
                "api_calls_today": 12345
            }
        }
        
        # JSON 응답 전송
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
        return
    
    def do_OPTIONS(self):
        # CORS preflight 요청 처리
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        return

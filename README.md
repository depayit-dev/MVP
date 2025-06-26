# Depayit MVP

MVP ระบบ Escrow ด้วย Flask + SQLite พร้อม deploy ขึ้น Render.com

## Endpoint
- POST `/create` – สร้างธุรกรรม
- POST `/confirm` – ยืนยันยอดโอน
- POST `/release` – ปล่อยเงินให้ผู้ขาย

## วิธี Deploy (Render)
1. เชื่อม GitHub กับ Render
2. กด New Web Service → เลือก repo นี้
3. ระบบจะ deploy อัตโนมัติตาม `render.yaml`

พร้อมใช้งาน!

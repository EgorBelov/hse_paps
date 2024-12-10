const express = require("express");
const multer = require("multer");
const path = require("path");

const app = express();

// Middleware для статичных файлов
app.use(express.static(path.join(__dirname, "public")));

// Конфигурация Multer
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "E:/HSE_HERNYA/hse_paps/Lab Work №3/uploads/");
    },
    filename: (req, file, cb) => {
        cb(null, `${Date.now()}-${file.originalname}`);
    },
});
const upload = multer({ storage });

// Маршрут для корневой страницы
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Маршрут для загрузки файлов
app.post("/api/upload", upload.single("file"), (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: "No file uploaded" });
    }

    res.json({
        message: "File uploaded successfully",
        filename: req.file.filename,
    });
});

// Запуск сервера
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

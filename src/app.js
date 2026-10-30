const os = require('os');
const express = require('express');

const app = express();
const port = process.env.PORT || 3000;

// Edit this message and push to trigger a new blue/green deployment
const MESSAGE = 'Hello from AWS CI/CD Capstone Project!';
const VERSION = process.env.APP_VERSION || 'v2';

app.disable('x-powered-by');

app.get('/', (req, res) => {
  res.type('html').send(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CI/CD Capstone</title>
  <style>
    body { margin:0; min-height:100vh; display:grid; place-items:center; background:#0b1f2a; color:#e8f1f2;
           font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
    main { background:#10303f; border:1px solid #1d4a5c; border-radius:12px; padding:32px 40px; text-align:center; }
    h1 { color:#2ec4b6; margin:0 0 12px; font-size:1.5rem; }
    .tag { display:inline-block; background:#ffb703; color:#1a1a1a; padding:2px 10px; border-radius:99px; font-weight:600; font-size:.8rem; }
    p { color:#8fb3bd; margin:10px 0 0; font-size:.9rem; }
  </style>
</head>
<body>
  <main>
    <h1>${MESSAGE}</h1>
    <span class="tag">${VERSION}</span>
    <p>Served by container ${os.hostname()}</p>
  </main>
</body>
</html>`);
});

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok' });
});

if (require.main === module) {
  app.listen(port, '0.0.0.0', () => {
    console.log(`App running on port ${port}`);
  });
}

module.exports = app;

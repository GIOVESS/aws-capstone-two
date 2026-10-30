const request = require('supertest');
const app = require('../src/app');

describe('app', () => {
  test('GET / returns the greeting page', async () => {
    const res = await request(app).get('/');
    expect(res.status).toBe(200);
    expect(res.headers['content-type']).toMatch(/html/);
    expect(res.text).toContain('Hello from AWS CI/CD Capstone Project!');
  });

  test('GET /health returns ok for the load balancer', async () => {
    const res = await request(app).get('/health');
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ status: 'ok' });
  });

  test('unknown route returns 404', async () => {
    const res = await request(app).get('/nope');
    expect(res.status).toBe(404);
  });
});

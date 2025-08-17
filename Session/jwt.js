const http = require('http');
const jwt = require('jsonwebtoken');

const SECRET_KEY = 'my-super-secret';

const user = {
  username: 'john11',
  password: '1234',
  role: 'admin'
};

// Async function to parse JSON body
async function getJSONBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => (body += chunk));
    req.on('end', () => {
      try {
        const parsed = JSON.parse(body);
        resolve(parsed);
      } catch (err) {
        reject(err);
      }
    });
  });
}

const server = http.createServer(async (req, res) => {
  if (req.url === '/login' && req.method === 'POST') {
    try {
      const parsedBody = await getJSONBody(req);

      if (parsedBody.username === user.username && parsedBody.password === user.password) {
        const token = jwt.sign(
          { username: user.username, role: user.role },
          SECRET_KEY,
          { expiresIn: '1h' }
        );
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ token }));
      } else {
        res.writeHead(401);
        res.end('Invalid credentials');
      }
    } catch (err) {
      res.writeHead(400);
      res.end('Invalid JSON');
    }
  }
  else if (req.url === '/posts' && req.method === 'GET') {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) {
      res.writeHead(401);
      return res.end('Token required');
    }

    try {
      const decoded = jwt.verify(token, SECRET_KEY);
      console.log(decoded);
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        message: 'Protected content: list of posts',
        user: decoded
      }));
    } catch (err) {
      res.writeHead(403);
      res.end('Invalid or expired token');
    }
  }
  else {
    res.writeHead(404);
    res.end('Not found');
  }
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});

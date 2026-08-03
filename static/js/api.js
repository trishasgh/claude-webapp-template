/* fetch wrapper + auth helpers */
var TOKEN_KEY = "app_token";
var USER_KEY = "app_user";

function api(path, opts) {
  opts = opts || {};
  var headers = (opts.headers = opts.headers || {});
  headers["Content-Type"] = "application/json";
  var token = localStorage.getItem(TOKEN_KEY);
  if (token && path.indexOf("/api/auth/") === -1) {
    headers["Authorization"] = "Bearer " + token;
  }
  return fetch(path, {
    method: opts.method || "GET",
    headers: headers,
    body: opts.body ? JSON.stringify(opts.body) : undefined,
  }).then(function (res) {
    return res.json().then(function (data) {
      if (!res.ok) {
        throw new Error((data && data.detail) || "Request failed");
      }
      return data;
    });
  });
}

function saveToken(token, username) {
  localStorage.setItem(TOKEN_KEY, token);
  localStorage.setItem(USER_KEY, username || "");
}

function getCurrentUser() {
  return localStorage.getItem(USER_KEY) || null;
}

function logout() {
  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
}

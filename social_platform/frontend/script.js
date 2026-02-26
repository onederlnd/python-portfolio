// --- base url of the api
const BASE_URL = "http://127.0.0.1:8000/api";

// --- create a user
async function createUser() {
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const bio = document.getElementById("bio").value;

  const response = await fetch(`${BASE_URL}/users`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({username, email, bio})
  });

  const data = await response.json();
  alert(`User created: ${JSON.stringify(data)}`);
}

// --- create a post
async function createPost() {
  const username = document.getElementById("post-username").value;
  const content = document.getElementById("post-content").value;

  const response = await fetch(`${BASE_URL}/posts`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({author: username, content})
  });

  const data = await response.json();
  alert(`Post created: ${JSON.stringify(data)}`);
}

// --- follow another user
async function followUser() {
  const follower = document.getElementById("follower").value;
  const followee = document.getElementById("followee").value;

  const response = await fetch(`${BASE_URL}/follow/${follower}/${followee}`, {
    method: "POST"
  });

  const data = await response.json();
  alert(`${follower} now follows ${followee}`);
}

// --- load feed
async function loadFeed() {
  const username = document.getElementById("feed-username").value;
  const response = await fetch(`${BASE_URL}/feed/${username}`);
  const posts = await response.json();

  const feedList = document.getElementById("feed-list");
  feedList.innerHTML = "";

  posts.forEach(post => {
    const postDiv = document.createElement("div");
    postDiv.textContent = `${post.author}: ${post.content} (${post.timestamp})`;
    feedList.appendChild(postDiv);
  });
}
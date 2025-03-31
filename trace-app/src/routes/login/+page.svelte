<script>
	import { goto } from '$app/navigation';
  
	let initials = "";
	let role = "Analyst";
	let message = "";
	let isError = false;
	let loading = false;
	// Testing
	async function handleSignIn() {
	  if (!initials.trim()) {
		message = "Please enter your initials.";
		isError = true;
		return;
	  }
//   
	  loading = true;
	  isError = false;
	  message = "";
  
	  try {
		const res = await fetch("/api/analyst/login", {
		  method: "POST",
		  headers: {
			"Content-Type": "application/json"
		  },
		  body: JSON.stringify({ initials, role })
		});
  
		const data = await res.json();
  
		if (!res.ok) {
		  message = data.detail || "Login failed.";
		  isError = true;
		} else {
		  message = `Signed in as ${data.initials} (${data.role})`;
		  isError = false;
  
		  // Store token and user info in localStorage
		  localStorage.setItem("token", data.access_token);
		  localStorage.setItem("initials", data.initials);
		  localStorage.setItem("role", data.role);
  
		  // Use SvelteKit's `goto` for redirection
		  goto('/dashboard');
		}
	  } catch (err) {
		console.error(err);
		message = "Unexpected error. Please try again.";
		isError = true;
	  }
  
	  loading = false;
  
	  setTimeout(() => {
		message = "";
	  }, 3000);
	}
  </script>
  
  <div class="container">
	<h1>Sign In</h1>
  
	{#if message}
	  <div class="toast {isError ? 'error' : 'success'}">{message}</div>
	{/if}
  
	<input
	  bind:value={initials}
	  class="input"
	  placeholder="Enter your initials"
	  on:keydown={(e) => e.key === 'Enter' && handleSignIn()}
	  required
	/>
  
	<select bind:value={role} class="dropdown">
	  <option value="Analyst">Analyst</option>
	  <option value="Lead">Lead</option>
	</select>
  
	{#if loading}
	  <button class="create-btn" disabled>Signing In...</button>
	{:else}
	  <button class="create-btn" on:click={handleSignIn}>Sign In</button>
	{/if}
  
	<a class="back-link" href="/">← Back to Home</a>
  </div>
  
  <style>
	@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@700&display=swap');
  
	:global(body) {
	  margin: 0;
	  background: linear-gradient(to bottom, #f4f4f4, #e5e5e5, #dcdcdc);
	  font-family: 'Raleway', sans-serif;
	}
  
	.container {
	  display: flex;
	  flex-direction: column;
	  align-items: center;
	  justify-content: center;
	  min-height: 100vh;
	  gap: 1rem;
	  padding: 1rem;
	}
  
	h1 {
	  font-size: 2.8rem;
	  margin-bottom: 1.5rem;
	  text-align: center;
	}
  
	.input,
	.dropdown {
	  padding: 0.75rem 1rem;
	  font-size: 1rem;
	  border-radius: 10px;
	  border: 1px solid #ddd;
	  width: 100%;
	  max-width: 280px;
	  outline: none;
	  box-sizing: border-box;
	  transition: border-color 0.25s ease, box-shadow 0.25s ease;
	  background-color: #fff;
	  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
	}
  
	.input:focus,
	.dropdown:focus {
	  border-color: #555;
	  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.05);
	}
  
	.dropdown {
	  appearance: none;
	  background-color: white;
	  background-image: url("data:image/svg+xml,%3Csvg fill='black' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M7 10l5 5 5-5z'/%3E%3C/svg%3E");
	  background-repeat: no-repeat;
	  background-position: right 1rem center;
	  background-size: 1rem;
	  padding-right: 2.5rem;
	}
  
	.create-btn {
	  padding: 0.75rem 1.5rem;
	  font-size: 1rem;
	  background-color: black;
	  color: white;
	  border: none;
	  border-radius: 10px;
	  cursor: pointer;
	  font-weight: 600;
	  width: 100%;
	  max-width: 280px;
	  transition: background-color 0.3s, transform 0.2s ease, box-shadow 0.2s ease;
	  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
	}
  
	.create-btn:hover {
	  background-color: #222;
	  transform: translateY(-3px) scale(1.03);
	  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
	}
  
	.back-link {
	  margin-top: 1rem;
	  color: #555;
	  text-decoration: none;
	  font-size: 0.95rem;
	  font-weight: 600;
	  transition: color 0.2s;
	}
  
	.back-link:hover {
	  color: #000;
	  text-decoration: underline;
	}
  
	.toast {
	  margin-top: 0.5rem;
	  text-align: center;
	  font-size: 0.95rem;
	  font-weight: 600;
	  padding: 0.75rem 1rem;
	  border-radius: 8px;
	  width: 100%;
	  max-width: 280px;
	  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
	  animation: fadeIn 0.3s ease-out;
	}
  
	.success {
	  background-color: #d4edda;
	  color: #155724;
	  border: 1px solid #c3e6cb;
	}
  
	.error {
	  background-color: #f8d7da;
	  color: #721c24;
	  border: 1px solid #f5c6cb;
	}
  
	@keyframes fadeIn {
	  from {
		opacity: 0;
		transform: translateY(-10px);
	  }
	  to {
		opacity: 1;
		transform: translateY(0);
	  }
	}
  </style>
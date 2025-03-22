<script lang="ts">
	import { goto } from '$app/navigation';

	function handleSignIn() {
		goto('/Login/Signin'); 
	}
</script>

<div class="trace-container">
	<div class="trace-inner">
		<span class="trace-left">TRA</span>
		<span class="trace-right">CE</span>
	</div>

	<button class="sign-in-button" on:click={handleSignIn}>
		Sign In
	</button>

	<a href="/Login/CreateAccount" class="new-account-link">
		New Account
	</a>
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@700&display=swap');
	@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
	.trace-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		height: 100vh;
		overflow: hidden;
		color: #000;
		background-color: transparent;
	}

	.trace-inner {
		font-family: 'Fredoka', sans-serif;
		font-weight: 700;
		font-size: clamp(3rem, 8vw, 10rem);
		display: flex;
	}

	.trace-left,
	.trace-right {
		opacity: 0;
		animation: slideIn 1s ease-out forwards;
	}

	.trace-left {
		animation-name: slideInLeft;
	}

	.trace-right {
		animation-name: slideInRight;
		animation-delay: 0.3s;
	}

	@keyframes slideInLeft {
		0% {
			transform: translateX(-100%);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}

	@keyframes slideInRight {
		0% {
			transform: translateX(100%);
			opacity: 0;
		}
		100% {
			transform: translateX(0);
			opacity: 1;
		}
	}

	.sign-in-button {
		margin-top: 2rem;
		padding: 0.75rem 2rem;
		font-size: 1.25rem;
		font-weight: 600;
		background-color: black;
		color: white;
		border: none;
		border-radius: 0.5rem;
		opacity: 0;
		transform: translateY(20px);
		animation: fadeInUp 1s ease forwards;
		animation-delay: 1s;
		cursor: pointer;
	}

	.new-account-link {
		margin-top: 1rem;
		font-size: 1rem;
		font-family: 'Montserrat', sans-serif;
		color: #444;
		text-decoration: underline;
		cursor: pointer;
		opacity: 0;
		transform: translateY(20px);
		animation: fadeInUp 1s ease forwards;
		animation-delay: 1.5s;
	}

	@keyframes fadeInUp {
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}
</style>
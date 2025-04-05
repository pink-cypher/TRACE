<script lang="ts">
	import './landing.css';
	import { goto } from '$app/navigation';
</script>

<div class="landing-container">
	<div class="left-panel">
		<div class="trace-inner">
			<span class="trace-left">TRA</span>
			<span class="trace-right">CE</span>
		</div>
	</div>

	<div class="divider"></div>

	<div class="right-panel">
		<div class="auth-box">
			<h2>Welcome</h2>
			<button class="auth-button" on:click={() => goto('/login')}>
				Sign In
			</button>
			<button class="auth-button secondary" on:click={() => goto('/create-account')}>
				Create Account
			</button>
		</div>
	</div>
</div>

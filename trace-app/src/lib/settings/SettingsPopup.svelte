<script>
	export let open = false;
	export let onClose = () => {};

	let exportFormat = localStorage.getItem("exportFormat") || "CSV";
	let theme = localStorage.getItem("theme") || "light";



	function saveSettings() {
		localStorage.setItem("exportFormat", exportFormat);
		localStorage.setItem("theme", theme);
		document.body.setAttribute("data-theme", theme);
		onClose();
	}

	function handleKeydown(e) {
		if (e.key === "Escape") {
			onClose();
		}
	}
</script>

{#if open}
	<div
		class="overlay"
		role="dialog"
		aria-modal="true"
		tabindex="-1"
		on:keydown={handleKeydown}
	>
		<!-- Transparent button over background to allow click-to-close (with keyboard support) -->
		<button
			class="overlay-dismiss"
			aria-label="Close settings"
			on:click={onClose}
			on:keydown={handleKeydown}
		></button>

		<!-- Popup content -->
		<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
		<!-- svelte-ignore a11y_click_events_have_key_events -->
		<div class="popup" role="document" on:click|stopPropagation>
			<button class="close-btn" on:click={onClose} aria-label="Close settings popup">×</button>
			<h2>Settings</h2>

			<div class="setting-group">
				<label for="exportFormat">Export Format:</label>
				<select id="exportFormat" bind:value={exportFormat}>
					<option value="CSV">CSV</option>
					<option value="XML">XML</option>
				</select>
			</div>
			<div class="setting-group">
				<label for="theme">Theme:</label>
				<select id="theme">
					<option value="light">Light</option>
					<option value="dark">Dark</option>
				</select>
			</div>

			<button class="save-btn" on:click={saveSettings}>Save</button>
		</div>
	</div>

{/if}


<style>
	.overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100vw;
		height: 100vh;
		background: rgba(0, 0, 0, 0.3);
		display: flex;
		align-items: center;
		justify-content: center;
		z-index: 999;
	}

	/* Invisible button to handle click-outside + keyboard accessibility */
	.overlay-dismiss {
		position: absolute;
		width: 100%;
		height: 100%;
		border: none;
		background: transparent;
		cursor: default;
		top: 0;
		left: 0;
	}

	.popup {
		background: #fff;
		border-radius: 12px;
		padding: 2rem;
		box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
		width: clamp(250px, 80vw, 360px); /* Responsive shrink */
		max-height: 90vh;
		overflow-y: auto;
		position: relative;
		animation: fadeIn 0.3s ease-out;
		z-index: 1000;
	}

	@keyframes fadeIn {
		from {
			transform: scale(0.95);
			opacity: 0;
		}
		to {
			transform: scale(1);
			opacity: 1;
		}
	}

	h2 {
		margin-top: 0;
		font-size: 1.5rem;
		text-align: center;
	}

	.setting-group {
		margin: 1rem 0;
		font-size: 0.95rem;
	}

	select {
		width: 100%;
		padding: 0.5rem;
		border-radius: 8px;
		border: 1px solid #ccc;
	}

	.save-btn {
		width: 100%;
		padding: 0.75rem;
		background: #000;
		color: white;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		transition: background 0.3s ease;
	}

	.save-btn:hover {
		background: #222;
	}

	.close-btn {
		position: absolute;
		top: 0.5rem;
		right: 0.75rem;
		background: none;
		border: none;
		font-size: 1.5rem;
		cursor: pointer;
		color: #555;
	}
</style>
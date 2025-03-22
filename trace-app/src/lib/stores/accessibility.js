// src/lib/stores/accessibility.js
import { writable } from 'svelte/store';
import { browser } from '$app/environment';

const initial = browser ? localStorage.getItem('colorBlindType') || 'none' : 'none';

export const colorBlindType = writable(initial);

// Persist changes only in the browser
if (browser) {
	colorBlindType.subscribe((value) => {
		localStorage.setItem('colorBlindType', value);
	});
}

// src/lib/stores/sessionStore.js
import { writable } from 'svelte/store';

export const initials = writable("");
export const role = writable(""); // "Lead" or "Analyst"
export const isLoggedIn = writable(false);

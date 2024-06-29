import App from './App.svelte';

// Create an instance of your Svelte application
const app = new App({
	target: document.body,
	props: {
		name: 'world' // Example prop
	}
});

// Export the Svelte app instance as the default export
export default app;

<script>
    import '../app.css';
    import { colorBlindType } from '$lib/stores/accessibility';
  </script>
  
  <div class={$colorBlindType}>
    <slot />
  </div>
  
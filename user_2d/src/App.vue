<template>
    <div id="app">
        <DrawRect></DrawRect>
    </div>
</template>

<script>
  import DrawRect from "./components/DrawRect";

  export default {
        name: 'App',
        components: {
            DrawRect,
        }
    }
</script>

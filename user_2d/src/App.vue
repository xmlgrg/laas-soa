<template>
    <div id="app">
        <DBDesigner></DBDesigner>
    </div>
</template>

<script>
  import DBDesigner from "./components/Workstation";

  export default {
        name: 'App',
        components: {
            DBDesigner,
        }
    }
</script>

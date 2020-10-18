<template>
    <div id="app" style="border: 0px;margin: 0px;padding: 0px;">
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
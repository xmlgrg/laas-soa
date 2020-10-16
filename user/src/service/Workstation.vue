<template>
  <div>
    <div style="height: 32px">
      <span style="margin-left: 2px;">LaasHubSOA</span>
      <ButtonGroup>
        <Button @click="onClickSwitchLayerTab" style="margin-left: 15px;">
          <Icon type="ios-arrow-forward"/>
          {{layer_name}}
        </Button>
        <Button @click="onClickSettings">Settings</Button>
        <Button @click="onClickHelp">Help</Button>
      </ButtonGroup>
    </div>
    <hr/>
    <Designer v-if="layer_name=='Dashboard'"></Designer>
    <Dashboard v-if="layer_name=='Designer'"></Dashboard>
  </div>
</template>

<script>
    import Designer from "./designer/Designer";
    import Dashboard from "./dashboard/Dashboard";

    const layer_name_designer = "Designer";
    const layer_name_dashboard = "Dashboard";


    export default {
        name: "Workstation",
        components: {Dashboard, Designer},
        data() {
            return {
                layer_name: layer_name_designer,
            }
        },
        methods: {
            onClickSwitchLayerTab: function () {
                if (this._data.layer_name == layer_name_designer) {
                    this._data.layer_name = layer_name_dashboard;
                } else {
                    this._data.layer_name = layer_name_designer;
                }
                localStorage.setItem('workstation_layer',this._data.layer_name);
            },
            onClickSettings: function () {
                this.$Message.info("Settings's page is not available");
            },
            onClickHelp: function () {
                this.$Message.info("Help's page is not available");
            },
        },
        created() {
            const last_workstation_layer = localStorage.getItem('workstation_layer');
            if (!last_workstation_layer) return;
            this._data.layer_name = last_workstation_layer;
        },
    }
</script>

<style>
  @import '~view-design/dist/styles/iview.css';
</style>

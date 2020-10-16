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
    <Designer v-if="if_layer.designer"></Designer>
    <Dashboard v-if="if_layer.dashboard"></Dashboard>
  </div>
</template>

<script>
    import Designer from "./designer/Designer";
    import Dashboard from "./dashboard/Dashboard";

    export default {
        name: "Workstation",
        components: {Dashboard, Designer},
        data() {
            return {
                layer_name: "Dashboard",
                if_layer: {
                    designer: true,
                    dashboard: false,
                },
            }
        },
        methods: {
            onClickSwitchLayerTab: function () {
                let item_key_array = Object.keys(this._data.if_layer);
                if (this._data.if_layer[item_key_array[0]]) {
                    this._data.if_layer[item_key_array[0]] = false;
                    this._data.if_layer[item_key_array[1]] = true;
                    this._data.layer_name = "Designer";
                } else {
                    this._data.if_layer[item_key_array[0]] = true;
                    this._data.if_layer[item_key_array[1]] = false;
                    this._data.layer_name = "Dashboard";
                }
            },
            onClickSettings: function () {
                this.$Message.info("Settings's page is not available");
            },
            onClickHelp: function () {
                this.$Message.info("Help's page is not available");
            },
        }
    }
</script>

<style>
  @import '~view-design/dist/styles/iview.css';
</style>

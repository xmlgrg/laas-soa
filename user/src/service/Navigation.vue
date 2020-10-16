<template>
  <div>
    <span style="margin-left: 15px;">LaasHubSOA</span>
    <Dropdown style="margin-left: 15px;">
      <a href="javascript:void(0)">DashBoard
        <Icon type="ios-arrow-down"></Icon>
      </a>
      <DropdownMenu slot="list">
        <DropdownItem>DashBoard</DropdownItem>
        <DropdownItem>Designer</DropdownItem>
      </DropdownMenu>
    </Dropdown>
    <a style="margin-left: 15px;">Settings</a>
    <a style="margin-left: 15px;">Help</a>
  </div>
</template>

<script>
    export default {
        name: "Navigation",
        data() {
            return {}
        }
    }
</script>

<style>
  @import '~view-design/dist/styles/iview.css';
</style>

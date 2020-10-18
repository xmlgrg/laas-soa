<template>
    <div>
    </div>
</template>
<script>
    import * as d3 from 'd3'

    export default {
        name: "DrawRect",
        mounted() {
            let width = window.innerWidth;
            let height = window.innerHeight;
            let svg = d3.select('div')
                .append('svg')
                .attr('width', width)
                .attr('height', height);

            svg.append("rect")  //添加一个矩形
                .attr("x", 50)
                .attr("y", 50)
                .attr("width", 50)
                .attr("height", 50)
                .attr("fill", "red")
        },
    }
</script>

<style scoped>
    .axis path,
    .axis line {
        fill: none;
        stroke: blue;
        shape-rendering: crispEdges;
    }

    .axis text {
        font-family: sans-serif;
        font-size: 11px;
    }
</style>
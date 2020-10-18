<template>
    <div>
    </div>
</template>
<script>
    import * as d3 from 'd3'

    export default {
        name: "DrawRect",
        mounted() {
            let width = 400;
            let height = 400;
            let svg = d3.select('div')
                .append('svg')
                .attr('width', width)
                .attr('height', height);
            var padding = {left: 30, right: 30, top: 20, bottom: 20};
            var dataset = [10, 20, 30, 40, 33, 24, 12, 5];
            var xScale = d3.scaleBand()
                .domain(d3.range(dataset.length))
                .rangeRound([0, width - padding.left - padding.right]);
            var yScale = d3.scaleLinear()
                .domain([0, d3.max(dataset)])
                .range([height - padding.top - padding.bottom, 0]);
            var xAxis = d3.axisBottom(xScale);
            var yAxis = d3.axisLeft(yScale);
            //添加x轴
            svg.append("g")
                .attr("class", "axis")
                .attr("transform", "translate(" + padding.left + "," + (height - padding.bottom) + ")")
                .call(xAxis);

//添加y轴
            svg.append("g")
                .attr("class", "axis")
                .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
                .call(yAxis);
            var rectPadding = 4;
            //添加矩形元素
            svg.selectAll(".MyRect")
                .data(dataset)
                .enter()
                .append("rect")
                .attr("class", "MyRect")
                .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
                .attr("x", function (d, i) {
                    return xScale(i) + rectPadding / 2;
                })
                .attr("y", function (d) {
                    return yScale(d);
                })
                .attr("width", xScale.bandwidth() - rectPadding)
                .attr("height", function (d) {
                    return height - padding.top - padding.bottom - yScale(d);
                }).attr("fill", "steelblue");

//添加文字元素
            svg.selectAll(".MyText")
                .data(dataset)
                .enter()
                .append("text")
                .attr("class", "MyText")
                .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
                .attr("x", function (d, i) {
                    return xScale(i) + rectPadding / 2;
                })
                .attr("y", function (d) {
                    var min = yScale.domain()[0];
                    return yScale(min);
                })
                .transition()
                .delay(function (d, i) {
                    return i * 200;
                })
                .duration(2000)
                .attr("y", function (d) {
                    return yScale(d);
                })
                .attr("dx", function () {
                    return (xScale.bandwidth() - rectPadding) / 2;
                })
                .attr("dy", function (d) {
                    return 20;
                })
                .text(function (d) {
                    return d;
                });
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
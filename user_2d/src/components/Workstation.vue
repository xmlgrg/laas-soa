<template>
    <div>
    </div>
</template>
<script>
    import * as d3 from 'd3'


    export default {
        name: "DBDesigner",
        mounted() {
            // base area
            let width = window.innerWidth;
            let height = window.innerHeight;
            let svg = d3.select('div')
                .append('svg')
                .attr('width', width)
                .attr('height', height);
            // global area
            const bdm = {
                draws_bdm: function (position) {
                    svg.append("rect")  //添加一个矩形
                        .attr("x", position.x)
                        .attr("y", position.y)
                        .attr("stroke-width", 2)
                        .attr("width", 50)
                        .attr("height", 50)
                        .attr("stroke", "black")
                        .attr("fill", "white")
                        .on("click", function () {
                            // d3.select(this).style("color", "red");
                            alert(1);
                        });
                }
            };

            document.oncontextmenu = function (event) { // make the chrome browser's right click don't show the page menu list
                event.preventDefault();
            };
            document.getElementsByTagName('svg')[0].onmousedown = function (e) {
                if (e.button == 2) { // right button click
                    // if already have dbm, do bdm's operation
                    bdm.draws_bdm({x: e.clientX, y: e.clientY});
                } else if (e.button == 0) { // left button click
                } else if (e.button == 1) { // scroll button click
                }
            }


        },
    }

</script>

<!--<style scoped>-->
<!--    .axis path,-->
<!--    .axis line {-->
<!--        fill: none;-->
<!--        stroke: blue;-->
<!--        shape-rendering: crispEdges;-->
<!--    }-->

<!--    .axis text {-->
<!--        font-family: sans-serif;-->
<!--        font-size: 11px;-->
<!--    }-->
<!--</style>-->
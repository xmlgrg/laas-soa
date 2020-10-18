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
                    let g = svg.append('g').on("click", function () {
                        // d3.select(this).style("color", "red");
                        // alert(1);
                    });
                    g.append("rect")  //添加一个矩形
                        .attr("x", position.x)
                        .attr("y", position.y)
                        .attr("stroke-width", 2)
                        .attr("width", 50)
                        .attr("height", 50)
                        .attr("stroke", "black")
                        .attr("fill", "white");
                    let bdm_name_text = '';
                    let appendBdmNameFunc = function () {
                        let foreignObject = svg.append("foreignObject")
                            .attr("x", position.x)
                            .attr("y", position.y - 20 - 2)
                            .attr("fill", "black")
                            .attr("width", 200)
                            .attr("height", 20)
                            .html(function (d) {
                                return '<input id="cur_input_id" type="text" value="' + bdm_name_text + '" autofocus="autofocus"/>'
                            }).on('keydown', function (event) {
                                let e = event || window.event || arguments.callee.caller.arguments[0];
                                if (e && e.keyCode == 13) {
                                    bdm_name_text = this.lastElementChild.value;
                                    bdm_name.text(bdm_name_text);
                                    this.remove()
                                }
                            });
                        document.getElementById('cur_input_id').focus();
                    };
                    let bdm_name = g.append('text').text(bdm_name_text).attr('fill', 'white')
                        .attr('x', position.x)
                        .attr('y', position.y - 10)
                        .attr('text-anchor', 'middle')
                        .style('font-size', '20px')
                        .attr("fill", "black")
                        .on('click', function (d, i) {
                            bdm_name.text('');
                            appendBdmNameFunc()
                        });
                    appendBdmNameFunc()

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
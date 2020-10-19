<template>
    <div style="border: 0px;margin: 0px;padding: 0px;">
    </div>
</template>
<script>
    import * as d3 from 'd3'


    export default {
        name: "DBDesigner",
        mounted() {
            // base area
            let width = window.screen.availWidth;
            let height = window.screen.availHeight;
            let svg = d3.select('div')
                .append('svg')
                .attr('width', '99vw')
                .attr('height', '97vh');
            // global area
            const bdm = {
                draws_bdm: function (position) {
                    let g = svg.append('g').on("click", function () {
                        // d3.select(this).style("color", "red");
                        // alert(1);
                    });
                    let d3_rect = g.append("rect")
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
                                return '<input id="cur_input_id" type="text" value="' + bdm_name_text + '" autofocus="autofocus"/>' + `test`
                            }).on('keydown', function (event) {
                                let e = event || window.event || arguments.callee.caller.arguments[0];
                                if (e && e.keyCode == 13) {
                                    let bdm_name_text_new = this.lastElementChild.value;
                                    if (bdm_name_text_new.length < 1) {
                                        alert("bdm's name can't be null");
                                        return;
                                    }
                                    let offset_length = (bdm_name_text_new.length - bdm_name_text.length) * 11.758 / 2;
                                    bdm_name_text = bdm_name_text_new;
                                    bdm_name.text(bdm_name_text);
                                    d3_rect.attr('width', parseInt(d3_rect.attr('width')) + offset_length);
                                    bdm_name.attr('x', parseInt(d3_rect.attr('x')) + bdm_name_text.length * 11.758 / 2);
                                    this.remove();
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
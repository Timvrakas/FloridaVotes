import parse
import export_for_viz
import logging

logging.log(10,"Starting test Script!")
lean = parse.parse()
export_for_viz.export_for_viz(lean)
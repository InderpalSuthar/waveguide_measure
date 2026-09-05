import pya

TRACE_WIDTH_UM = 10.0

def measure_total_length_only():
    app = pya.Application.instance()
    mw = app.main_window()
    view = mw.current_view()

    if view is None or not list(view.each_object_selected()):
        pya.MessageBox.warning("Warning", "No waveguide objects selected!", pya.MessageBox.Ok)
        return

    total_path_length_um = 0.0

    for obj in view.each_object_selected():
        if obj.is_cell_inst():
            continue

        shape = obj.shape
        dbu = view.cellview(obj.cv_index).layout().dbu

        if shape.is_box() or shape.is_polygon():
            box = shape.bbox()
            dx_um = box.width() * dbu
            dy_um = box.height() * dbu

            actual_width_um = min(dx_um, dy_um)

            if (
                abs(actual_width_um - TRACE_WIDTH_UM) > 0.1
                and shape.polygon.area() * (dbu**2) > 0
            ):
                area_um2 = shape.polygon.area() * (dbu**2)
                length_um = area_um2 / TRACE_WIDTH_UM
            else:
                length_um = max(dx_um, dy_um)

            total_path_length_um += length_um

    pya.MessageBox.info(
        "Waveguide Length", 
        f"Total Path Length: {total_path_length_um:.3f} µm", 
        pya.MessageBox.Ok
    )
from pathlib import Path
import ast
import numpy as np
import pandas as pd


SOURCE = Path(__file__).with_name("streamlit_app.py")


def load_functions():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    wanted = {"interval_audit_metrics"}
    body = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in wanted]
    ns = {
        "np": np, "pd": pd,
    }
    exec(compile(ast.Module(body=body, type_ignores=[]), str(SOURCE), "exec"), ns)
    return ns


def run():
    ns = load_functions()
    fps, total = 20.0, 100
    df = pd.DataFrame({"frame": np.arange(total)})

    source_text = SOURCE.read_text(encoding="utf-8")
    assert 'cap.set(cv2.CAP_PROP_POS_FRAMES, first_frame)' in source_text
    assert 'if last_frame is not None and frame_no > last_frame:' in source_text
    assert 'render_angle_video(Path(st.session_state.video1_path), seg,' in source_text
    assert 'render_angle_video(Path(st.session_state.video1_path), seg_front,' in source_text
    assert 'render_angle_video(Path(st.session_state.video2_path), seg_lat,' in source_text

    audit = ns["interval_audit_metrics"](df.iloc[20:40].copy(), fps, 1.0, 1.95)
    values = {m["key"]: m["value"] for m in audit}
    assert values["analyzed_first_frame"] == 20
    assert values["analyzed_last_frame"] == 39
    assert values["analyzed_frame_count"] == 20
    assert abs(values["analyzed_interval_duration_s"] - 1.0) < 1e-9
    print("OK: V166 interval audit and annotated-video crop wiring passed")


if __name__ == "__main__":
    run()

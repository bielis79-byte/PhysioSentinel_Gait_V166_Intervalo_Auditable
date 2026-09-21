from pathlib import Path
import ast
import numpy as np


SOURCE = Path(__file__).with_name("streamlit_app.py")
WANTED = {
    "_metric_record", "_metric_float", "_metric_is_usable", "_metric_value_any",
    "_metric_mean_any", "_score_lower_better", "_score_higher_better", "_score_band",
    "_mean_valid", "_index_classification", "_biomech_classification",
    "_domain_classification", "_infer_biomech_context", "_pair_score_from_lr",
    "_sagittal_joint_symmetry", "compute_biomechanical_profile",
    "_functional_support_score", "_assistive_device_score", "_effective_support_score",
    "compute_locomotor_capacity_index",
}


def load_functions():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    body = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in WANTED]
    ns = {"np": np}
    exec(compile(ast.Module(body=body, type_ignores=[]), str(SOURCE), "exec"), ns)
    return ns


def metric(key, value, quality="Alta"):
    return {"key": key, "value": value, "quality": quality}


def locomotor_metrics(cadence=100.0, cv=5.0, similarity=100.0, temporal_asym=5.0, stance_asym=5.0):
    return [
        metric("cadence_exp", cadence), metric("regularity_cv", cv),
        metric("step_to_step_similarity_index", similarity),
        metric("temporal_asymmetry_exp", temporal_asym), metric("stance_asymmetry_2d", stance_asym),
        metric("tracking_mean", 0.90), metric("straight_walking_usable_pct", 95.0),
        metric("step_count_consistency_error_pct", 5.0),
    ]


def frontal_metrics():
    rows = [
        metric("pelvis_obliquity_rom", 2.0), metric("pelvis_obliquity_p95_abs", 1.0),
        metric("pelvis_obliquity_side_asymmetry_pct", 5.0), metric("pelvis_cycle_consistency_index", 95.0),
        metric("trunk_lateral_lean_rom", 2.0), metric("trunk_lateral_lean_p95_abs", 1.0),
        metric("trunk_lateral_lean_side_asymmetry_pct", 5.0), metric("trunk_cycle_consistency_index", 95.0),
        metric("shoulder_obliquity_rom", 3.0), metric("shoulder_obliquity_p95_abs", 2.0),
        metric("shoulder_obliquity_side_asymmetry_pct", 5.0), metric("shoulder_cycle_consistency_index", 95.0),
        metric("shoulder_pelvis_rel_rom", 3.0), metric("shoulder_pelvis_rel_p95_abs", 2.0),
        metric("shoulder_pelvis_cycle_consistency_index", 95.0),
        metric("com_lateral_excursion_norm_pct", 20.0), metric("com_bos_ratio_p95", 0.40),
        metric("com_lateral_side_asymmetry_pct", 5.0), metric("com_lateral_cycle_consistency_index", 95.0),
        metric("com_bos_cycle_consistency_index", 95.0),
        metric("frontal_knee_dev_l_p95", 16.0), metric("frontal_knee_dev_r_p95", 18.0),
        metric("dynamic_knee_valgus_l_deg", 8.0), metric("dynamic_knee_valgus_r_deg", 10.0),
        metric("foot_progress_l_median", -30.0), metric("foot_progress_r_median", 35.0),
        metric("rearfoot_tilt_l_p95", 8.0), metric("rearfoot_tilt_r_p95", 24.0),
        metric("tracking_mean", 0.90), metric("straight_walking_usable_pct", 95.0),
    ]
    return rows


def run():
    ns = load_functions()
    locomotor = ns["compute_locomotor_capacity_index"]
    biomech = ns["compute_biomechanical_profile"]

    normal = locomotor(locomotor_metrics(), "Independiente", 1.20, "Sin ayuda")
    assert normal["score"] >= 95.0, normal

    crutches = locomotor(locomotor_metrics(), "Independiente", 0.0, "2 muletas")
    assert crutches["score"] <= 49.0, crutches
    assert crutches["effective_support_score"] == 35.0, crutches
    assert any("2 muletas" in cap for cap in crutches["caps"]), crutches

    slow_cadence = locomotor(locomotor_metrics(cadence=45.0), "Independiente", 0.0, "Sin ayuda")
    assert slow_cadence["score"] <= 49.0, slow_cadence
    assert "Ritmo locomotor" in slow_cadence["components"], slow_cadence

    slow_speed = locomotor(locomotor_metrics(), "Independiente", 0.30, "Sin ayuda")
    assert slow_speed["score"] <= 49.0, slow_speed

    profile = biomech(frontal_metrics(), analysis_mode="1 cámara · 2D", view="Frontal/posterior")
    assert "Control distal proyectado de rodilla y pie" in profile["domains"], profile
    assert profile["domains"]["Control distal proyectado de rodilla y pie"] < 50.0, profile
    assert profile["global_score"] < 70.0, profile
    assert abs(sum(profile["domain_weights"].values()) - 1.0) < 1e-9, profile

    print("OK: ICLM 0.2 and ICBF 0.5 regression tests passed")
    print("normal", round(normal["score"], 2))
    print("two_crutches", round(crutches["score"], 2), crutches["caps"])
    print("slow_cadence", round(slow_cadence["score"], 2), slow_cadence["caps"])
    print("pau_like_biomech", round(profile["global_score"], 2), profile["domains"])


if __name__ == "__main__":
    run()

"""Comprobación estática de las garantías de exportación V164."""
from pathlib import Path
import ast,json

root=Path(__file__).resolve().parent
app=(root/'streamlit_app.py').read_text(encoding='utf-8')
skel=(root/'skel_poc.py').read_text(encoding='utf-8')
ast.parse(app); ast.parse(skel)

checks={
    'app_version_164':'APP_VERSION = "164"' in app,
    'quality_csv':'calidad_captura_completa.csv' in app,
    'quality_json':'calidad_captura_completa.json' in app,
    'report_docx':'informe_completo.docx' in app,
    'report_pdf':'informe_completo.pdf' in app,
    'history_plot_png':'grafica_evolucion_seleccionada.png' in app,
    'profile_plot_png':'grafica_perfil_biomecanico.png' in app,
    'corrected_skin_npz':'piel_SKEL_V163_corregida_75frames.npz' in app,
    'denver_compact_npz':'denver_geometria_transformaciones_compactas.npz' in app,
    'tab12_exports':'P12_Cinematica_Anatomica_3D' in app,
    'tab13_exports':'P13_Analisis_Musculoesqueletico_3D' in app,
    'coverage_14_tabs':'MANIFEST_V164_COBERTURA_14_PESTANAS.json' in app and '"pestaña":14' in app,
    'viewer_publishes_corrected_skin':'v164_corrected_skin_export' in skel,
    'official_gender_weights':'v163_official_skin_data' in skel,
    'kinematics_assignment_absent':'mesh_seq["poses"]=' not in skel and "mesh_seq['poses']=" not in skel,
    'private_assets_absent':not any(root.rglob('skel_male.pkl')) and not any(root.rglob('skel_female.pkl')),
}
result={'version':'164','pass':all(checks.values()),'checks':checks}
(root/'VALIDACION_EXPORTACION_V164.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(0 if result['pass'] else 1)

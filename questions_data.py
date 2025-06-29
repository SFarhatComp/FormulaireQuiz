FORMS_DATA = {
    "FORM_1": {
        "title": "Medical History",
        "questions": [
            "Patient Code", "Blood group", "RH",
            {"label": "Allergies?", "type": "yesno"},
            "Taille", "Poids",
            {"label": "NHYA?", "type": "yesno"},
            {"label": "Angina?", "type": "yesno"},
            {"label": "Syncope?", "type": "yesno"},
            {"label": "Family history?", "type": "yesno"},
            {
                "label": "Congenital Malformation?",
                "type": "yesno_conditional",
                "hides": [
                    "Congenital: APVR?", "Congenital: Coarctaction?", "Congenital: Coronary artery anomalies?",
                    "Congenital: VSD?", "Congenital: ASD?", "Congenital: Subaortic membrane?", "Notes congenital"
                ],
                "fill_value": "0"
            },
            {"label": "Congenital: APVR?", "type": "yesno"},
            {"label": "Congenital: Coarctaction?", "type": "yesno"},
            {"label": "Congenital: Coronary artery anomalies?", "type": "yesno"},
            {"label": "Congenital: VSD?", "type": "yesno"},
            {"label": "Congenital: ASD?", "type": "yesno"},
            {"label": "Congenital: Subaortic membrane?", "type": "yesno"},
            "Notes congenital",
            {"label": "Diabetes?", "type": "yesno"},
            {"label": "DLP?", "type": "yesno"},
            {"label": "HTN?", "type": "yesno"},
            {"label": "Obesity?", "type": "yesno"},
            {"label": "COPD?", "type": "yesno"},
            {"label": "Is it a redo?", "type": "yesno"},
            "Date of last cardiac surgery", "Details if redo",
            {"label": "CAD?", "type": "yesno"},
            {"label": "Unstable angina?", "type": "yesno"},
            {"label": "Previous MI?", "type": "yesno"},
            {"label": "AF?", "type": "yesno"},
            {"label": "PVD?", "type": "yesno"},
            {"label": "Smoking?", "type": "yesno"},
            {"label": "History of rhumatismal disease?", "type": "yesno"}
        ]
    },
    "FORM_2": {
        "title": "PreOP State Evaluation",
        "questions": [
            "Creatinine clearance (umol/L)",
            {"label": "CKD?", "type": "yesno"},
            {"label": "Neurological dysfunction?", "type": "yesno"},
            {"label": "Critical state?", "type": "yesno"},
            {"label": "Pulmonary HTN?", "type": "yesno"},
            "Preop PAP", "Level of emergency (1= elective, 2= emergent, 3=urgent, 4=salvage)",
            {"label": "Preop need for ventilation support?", "type": "yesno"},
            "KT EF (%)", "KT Systolic pressure (mm Hg)", "KT Diastolic pressure (mm Hg)", "Preop cardiac rythm", "Other comorbidities"
        ]
    },
    "FORM_3": {
        "title": "Valve Lesion",
        "questions": [
            {"label": "Aortic stenosis?", "type": "yesno"},
            {"label": "Aortic regurgitation?", "type": "yesno"},
            {"label": "Mixed stenosis/regurgitation?", "type": "yesno"},
            "If mixed, predominance? (1=AR, 2=AS, 3=Balanced)",
            {"label": "Endocarditis?", "type": "yesno"},
            "Status of endocarditis? (1=Active, 2=Recently cured, 3=Past)",
            {"label": "Ascending aorta aneuvrysm?", "type": "yesno"},
            {"label": "Aortic root aneuvrysm?", "type": "yesno"},
            {"label": "Rhumatic disease?", "type": "yesno"},
            "Other related to valve lesion"
        ]
    },
    "FORM_4": {
        "title": "Pre op Echo",
        "questions": [
            "Date of preop echo (YYYY-MM-DD)", "BSA", "Preop EF", "LV mass (g)", "Diastolic LV diameter (mm)", "Systolic LV diameter (mm)", "IVS (mm)", "LVPFW (mm)", "Mean AV gradient (mm Hg)", "Max AV gradient (mm Hg)", "AVA", "Index AVA", "Max velocity (m/s)", "AR level", "PR level", "Pulmonary peak gradient max (mm Hg)", "Pulmonary gradient mean (mm Hg)", "Annulus aorta (mm)", "Valsalva sinus (mm)", "Ascending aorta (mm)", "ST junction (mm)", "MR level", "TR level", "Mitral gradient (mm Hg)", "Associated lesion"
        ]
    },
    "FORM_5": {
        "title": "Operative Data",
        "questions": [
            "CPB time (min)", "Clamp time (min)", "Reprfusion time (min)", "Circulatory arrest time (min)", "Time of circulatory arrest", "Cardioplegia type (1=antegrade, 2=retrograde, 3=both)",
            {"label": "Del Nido cardioplegia?", "type": "yesno"},
            "Temperature (celsius)", "Surgery duration (min)", "Other",
            {"label": "Intraoperative death?", "type": "yesno"},
            "Surgery approach (1= full sternotomy, 2= upper hemisternotomy, 3= right-anterior minithoracotomy)", "Surgical graft model", "Surgical graft size (mm)", "AV morphology (1=uni, 2-bi, 3=tri, 4=quadri, 5= prosthesis)", "Bicuspid phenotype (1=R-L, 2=R-N)", "Sievers classification",
            {"label": "Isolated AVR?", "type": "yesno"},
            {"label": "Associated procedures?", "type": "yesno"},
            "Number of associated procedures?",
            {"label": "Ascending aorta replacement?", "type": "yesno"},
            "Ascending aorta replacement size",
            {"label": "Hemiarch replacement?", "type": "yesno"},
            "Hemiarch replacement size",
            {"label": "MV repair?", "type": "yesno"},
            {"label": "CABG?", "type": "yesno"},
            {"label": "TV repair?", "type": "yesno"},
            "Other associated procedures"
        ]
    },
    "FORM_6": {
        "title": "PostUp Early Outcomes",
        "questions": [
            "ICU stay (days)", "Date of discharge", "LOS (days)", "Creatinine max (umol/L)",
            {"label": "CVVH?", "type": "yesno"},
            {"label": "Reintervention needed for bleeding?", "type": "yesno"},
            {"label": "Transfusion?", "type": "yesno"},
            "PRBC qty", "Platelets qty", "Cryo", "FFP qty", "Intubation duration (1= less than 24h, 2= 24 to48h, 3= more than 48h)",
            {"label": "Reintubation?", "type": "yesno"},
            {"label": "Delirium?", "type": "yesno"},
            {"label": "Stroke?", "type": "yesno"},
            {"label": "TIA?", "type": "yesno"},
            {"label": "OAP?", "type": "yesno"},
            {"label": "Low output?", "type": "yesno"},
            "CKMB value ug/L", "PMP",
            {"label": "FA or flutter?", "type": "yesno"},
            {"label": "MI?", "type": "yesno"},
            {"label": "Mediastinitis?", "type": "yesno"},
            {"label": "DSW infection?", "type": "yesno"},
            {"label": "Pulmonary infection?", "type": "yesno"},
            {"label": "Beta blocker?", "type": "yesno"},
            {"label": "Losartan?", "type": "yesno"},
            {"label": "ACEI?", "type": "yesno"},
            {"label": "CCB?", "type": "yesno"},
            {"label": "Naproxen?", "type": "yesno"},
            {"label": "Other Rx?", "type": "yesno"},
            {"label": "Other complications", "type": "yesno"},
            {"label": "Death?", "type": "yesno"},
            "Date of death", "STS death classification (1=. valve-related, 2= sudden/unexplained, 3= cardiac, 4= other)", "Cause of death"
        ]
    },
    "FORM_7": {
        "title": "PostOP Echo 1",
        "questions": [
            "Date of postop echo", "BSA", "LVSD (mm)", "LVDD (mm)", "Ejection fraction (%)", "LV mass indexed (g/m2)", "LVPFW (mm)", "IVS (mm)", "Mean AV gradient (mm Hg)", "Max AV gradient (mm Hg)", "AVA (cm2)", "AVA index", "iAVA (cm2/m2)", "Max velocity (m/s)", "AR (0, 0.5, 1, 2, 3, 4)", "MR (0, 0.5, 1, 2, 3, 4)", "TR (0, 0.5, 1, 2, 3, 4)", "PR (0, 0.5, 1, 2, 3, 4)", "Pulmonary peak gradient (mm Hg)", "Pulmonary mean gradient (mm Hg)", "Anneau (mm)", "Valsalva (mm)", "ST junction (mm)", "Ascending aorta (mm)"
        ]
    },
    "FORM_8": {
        "title": "PostOp MRI",
        "questions": [
            {
                "label": "Postop MRI?",
                "type": "yesno_conditional",
                "hides": [
                    "Date of MRI", "LV ejection fraction (%)", "LV telediastolic volume (mL)", "LV telesystolic volume (mL)", "LV mass (g)", "RV ejection fraction (%)", "RV telediastolic volume (mL)", "RV telesystolic volume (mL)", "AV regurgitation fraction (%)", "PV regurgitation fraction (%)", "Aortic annulus (mm)", "Valsalva sinus (mm)", "ST junction (mm)", "Tubular aorta (mm)", "Postop MRI notes"
                ],
                "fill_value": "N/A"
            },
            "Date of MRI", "LV ejection fraction (%)", "LV telediastolic volume (mL)", "LV telesystolic volume (mL)", "LV mass (g)", "RV ejection fraction (%)", "RV telediastolic volume (mL)", "RV telesystolic volume (mL)", "AV regurgitation fraction (%)", "PV regurgitation fraction (%)", "Aortic annulus (mm)", "Valsalva sinus (mm)", "ST junction (mm)", "Tubular aorta (mm)", "Postop MRI notes"
        ]
    },
    "FORM_9": {
        "title": "Follow Up Echo 1",
        "preliminary_question": "Has he done a Follow Up Echo 1?",
        "fill_value": "N/A",
        "questions": [
            "Date of follow up echo", "BSA", "LVSD (mm)", "LVDD (mm)", "Ejection fraction (%)", "LV mass indexed (g/m2)", "LVPFW (mm)", "IVS (mm)", "Mean AV gradient (mm Hg)", "Max AV gradient (mm Hg)", "AVA (cm2)", "AVA index", "Max velocity (m/s)", "AR (0, 0.5, 1, 2, 3, 4)", "MR (0, 0.5, 1, 2, 3, 4)", "TR (0, 0.5, 1, 2, 3, 4)", "Pulmonary peak gradient (mm Hg)", "PR (0, 0.5, 1, 2, 3, 4)", "Pulmonary mean gradient (mm Hg)", "Anneau (mm)", "Valsalva (mm)", "ST junction (mm)", "Ascending aorta (mm)"
        ]
    },
    "FORM_10": {
        "title": "Follow Up Echo 2",
        "preliminary_question": "Has he done a Follow Up Echo 2?",
        "fill_value": "N/A",
        "questions": [
            "Date of follow up echo", "BSA", "LVSD (mm)", "LVDD (mm)", "Ejection fraction (%)", "LV mass indexed (g/m2)", "LVPFW (mm)", "IVS (mm)", "Mean AV gradient (mm Hg)", "Max AV gradient (mm Hg)", "AVA (cm2)", "AVA index", "Max velocity (m/s)", "AR (0, 0.5, 1, 2, 3, 4)", "MR (0, 0.5, 1, 2, 3, 4)", "TR (0, 0.5, 1, 2, 3, 4)", "Pulmonary peak gradient (mm Hg)", "PR (0, 0.5, 1, 2, 3, 4)", "Pulmonary mean gradient (mm Hg)", "Anneau (mm)", "Valsalva (mm)", "ST junction (mm)", "Ascending aorta (mm)"
        ]
    },
    "FORM_11": {
        "title": "Follow Up Echo 3",
        "preliminary_question": "Has he done a Follow Up Echo 3?",
        "fill_value": "N/A",
        "questions": [
            "Date of follow up echo", "BSA", "LVSD (mm)", "LVDD (mm)", "Ejection fraction (%)", "LV mass indexed (g/m2)", "LVPFW (mm)", "IVS (mm)", "Mean AV gradient (mm Hg)", "Max AV gradient (mm Hg)", "AVA (cm2)", "AVA index", "Max velocity (m/s)", "AR (0, 0.5, 1, 2, 3, 4)", "MR (0, 0.5, 1, 2, 3, 4)", "TR (0, 0.5, 1, 2, 3, 4)", "Pulmonary peak gradient (mm Hg)", "PR (0, 0.5, 1, 2, 3, 4)", "Pulmonary mean gradient (mm Hg)", "Anneau (mm)", "Valsalva (mm)", "ST junction (mm)", "Ascending aorta (mm)"
        ]
    },
    "FORM_12": {
        "title": "Post OP Clinical Follow Up Data (3 months)",
        "questions": [
            "Follow up date", "NYHA (1, 2, 3, 4)",
            {"label": "Complications?", "type": "yesno"},
            {"label": "TIA?", "type": "yesno"},
            {"label": "Stroke?", "type": "yesno"},
            {"label": "Systemic embolism?", "type": "yesno"},
            "Date of embolism",
            {"label": "MI?", "type": "yesno"},
            "Date of MI",
            {"label": "Rehospitalisation for heart failure?", "type": "yesno"},
            {"label": "Bleeding", "type": "yesno"},
            "Description of bleeding", "Date of bleeding",
            {"label": "Endocarditis", "type": "yesno"},
            "Date of endocarditis",
            {"label": "Arrythmia: AF?", "type": "yesno"},
            {"label": "Arrythmia: AVB?", "type": "yesno"},
            {"label": "Arrythmia: PMP?", "type": "yesno"},
            {"label": "Arrythmia: Other?", "type": "yesno"},
            {"label": "Arrythmia: None?", "type": "yesno"},
            "Date of arrythmia",
            {"label": "Reintervention needed?", "type": "yesno"},
            "Cause of reintervention", "Date of reintervention",
            {"label": "Death?", "type": "yesno"},
            "STS classification of death (1=valve-related, 2=sudden/unexplained, 3=cardiac, 4=other)", "Date of death"
        ]
    },
    "FORM_13": {
        "title": "Latest Clinical Data",
        "questions": [
            "Latest clinical data DATE", "NYHA (1, 2, 3, 4)",
            {"label": "Complications?", "type": "yesno"},
            {"label": "TIA?", "type": "yesno"},
            {"label": "Stroke?", "type": "yesno"},
            {"label": "Systemic embolism?", "type": "yesno"},
            "Date of embolism",
            {"label": "MI?", "type": "yesno"},
            "Date of MI",
            {"label": "Rehospitalisation for heart failure?", "type": "yesno"},
            {"label": "Bleeding", "type": "yesno"},
            "Description of bleeding", "Date of bleeding",
            {"label": "Endocarditis", "type": "yesno"},
            "Date of endocarditis",
            {"label": "Arrythmia: AF?", "type": "yesno"},
            {"label": "Arrythmia: AVB?", "type": "yesno"},
            {"label": "Arrythmia: PMP?", "type": "yesno"},
            {"label": "Arrythmia: Other?", "type": "yesno"},
            {"label": "Arrythmia: None?", "type": "yesno"},
            "Date of arrythmia",
            {"label": "Reintervention needed?", "type": "yesno"},
            "Cause of reintervention", "Date of reintervention",
            {"label": "Death?", "type": "yesno"},
            "STS classification of death (1=valve-related, 2=sudden/unexplained, 3=cardiac, 4=other)", "Date of death"
        ]
    }
} 
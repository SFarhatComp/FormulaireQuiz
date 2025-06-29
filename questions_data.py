FORMS_DATA = {
    "FORM_1": {
        "title": "Medical History",
        "questions": [
            "Patient Code", "Blood group", "RH", "Allergies?", "Taille", "Poids", "NHYA?", "Angina?", "Syncope?", "Family history?",
            {
                "label": "Congenital Malformation?",
                "type": "yesno_conditional",
                "hides": [
                    "Congenital: APVR?", "Congenital: Coarctaction?", "Congenital: Coronary artery anomalies?",
                    "Congenital: VSD?", "Congenital: ASD?", "Congenital: Subaortic membrane?", "Notes congenital"
                ],
                "fill_value": "0"
            },
            "Congenital: APVR?", "Congenital: Coarctaction?", "Congenital: Coronary artery anomalies?", "Congenital: VSD?", "Congenital: ASD?", "Congenital: Subaortic membrane?", "Notes congenital",
            "Diabetes?", "DLP?", "HTN?", "Obesity?", "COPD?", "Is it a redo?", "Date of last cardiac surgery", "Details if redo", "CAD?", "Unstable angina?", "Previous MI?", "AF?", "PVD?", "Smoking?", "History of rhumatismal disease?"
        ]
    },
    "FORM_2": {
        "title": "PreOP State Evaluation",
        "questions": [
            "Creatinine clearance (umol/L)", "CKD?", "Neurological dysfunction?", "Critical state?", "Pulmonary HTN?", "Preop PAP", "Level of emergency (1= elective, 2= emergent, 3=urgent, 4=salvage)", "Preop need for ventilation support?", "KT EF (%)", "KT Systolic pressure (mm Hg)", "KT Diastolic pressure (mm Hg)", "Preop cardiac rythm", "Other comorbidities"
        ]
    },
    "FORM_3": {
        "title": "Valve Lesion",
        "questions": [
            "Aortic stenosis?", "Aortic regurgitation?", "Mixed stenosis/regurgitation?", "If mixed, predominance? (1=AR, 2=AS, 3=Balanced)", "Endocarditis?", "Status of endocarditis? (1=Active, 2=Recently cured, 3=Past)", "Ascending aorta aneuvrysm?", "Aortic root aneuvrysm?", "Rhumatic disease?", "Other related to valve lesion"
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
            "CPB time (min)", "Clamp time (min)", "Reprfusion time (min)", "Circulatory arrest time (min)", "Time of circulatory arrest", "Cardioplegia type (1=antegrade, 2=retrograde, 3=both)", "Del Nido cardioplegia?", "Temperature (celsius)", "Surgery duration (min)", "Other", "Intraoperative death?", "Surgery approach (1= full sternotomy, 2= upper hemisternotomy, 3= right-anterior minithoracotomy)", "Surgical graft model", "Surgical graft size (mm)", "AV morphology (1=uni, 2-bi, 3=tri, 4=quadri, 5= prosthesis)", "Bicuspid phenotype (1=R-L, 2=R-N)", "Sievers classification", "Isolated AVR?", "Associated procedures?", "Number of associated procedures?", "Ascending aorta replacement?", "Ascending aorta replacement size", "Hemiarch replacement?", "Hemiarch replacement size", "MV repair?", "CABG?", "TV repair?", "Other associated procedures"
        ]
    },
    "FORM_6": {
        "title": "PostUp Early Outcomes",
        "questions": [
            "ICU stay (days)", "Date of discharge", "LOS (days)", "Creatinine max (umol/L)", "CVVH?", "Reintervention needed for bleeding?", "Transfusion?", "PRBC qty", "Platelets qty", "Cryo", "FFP qty", "Intubation duration (1= less than 24h, 2= 24 to48h, 3= more than 48h)", "Reintubation?", "Delirium?", "Stroke?", "TIA?", "OAP?", "Low output?", "CKMB value ug/L", "PMP", "FA or flutter?", "MI?", "Mediastinitis?", "DSW infection?", "Pulmonary infection?", "Beta blocker?", "Losartan?", "ACEI?", "CCB?", "Naproxen?", "Other Rx?", "Other complications", "Death?", "Date of death", "STS death classification (1=. valve-related, 2= sudden/unexplained, 3= cardiac, 4= other)", "Cause of death"
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
            "Follow up date", "NYHA (1, 2, 3, 4)", "Complications?", "TIA?", "Stroke?", "Systemic embolism?", "Date of embolism", "MI?", "Date of MI", "Rehospitalisation for heart failure?", "Bleeding", "Description of bleeding", "Date of bleeding", "Endocarditis", "Date of endocarditis", "Arrythmia: AF?", "Arrythmia: AVB?", "Arrythmia: PMP?", "Arrythmia: Other?", "Arrythmia: None?", "Date of arrythmia", "Reintervention needed?", "Cause of reintervention", "Date of reintervention", "Death?", "STS classification of death (1=valve-related, 2=sudden/unexplained, 3=cardiac, 4=other)", "Date of death"
        ]
    },
    "FORM_13": {
        "title": "Latest Clinical Data",
        "questions": [
            "Latest clinical data DATE", "NYHA (1, 2, 3, 4)", "Complications?", "TIA?", "Stroke?", "Systemic embolism?", "Date of embolism", "MI?", "Date of MI", "Rehospitalisation for heart failure?", "Bleeding", "Description of bleeding", "Date of bleeding", "Endocarditis", "Date of endocarditis", "Arrythmia: AF?", "Arrythmia: AVB?", "Arrythmia: PMP?", "Arrythmia: Other?", "Arrythmia: None?", "Date of arrythmia", "Reintervention needed?", "Cause of reintervention", "Date of reintervention", "Death?", "STS classification of death (1=valve-related, 2=sudden/unexplained, 3=cardiac, 4=other)", "Date of death"
        ]
    }
} 
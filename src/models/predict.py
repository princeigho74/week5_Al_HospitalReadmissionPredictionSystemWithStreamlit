import React, { useState } from 'react';
import { ArrowDown, Database, GitBranch, CheckCircle, Settings, TrendingUp, AlertTriangle, Users, FileText, Brain, Target, RefreshCw, ChevronRight, Info, AlertCircle, CheckSquare, X } from 'lucide-react';

export default function AIWorkflowDiagram() {
  const [selectedStage, setSelectedStage] = useState(null);
  const [expandedStage, setExpandedStage] = useState(null);
  const [showFeedback, setShowFeedback] = useState(false);
  const [completedStages, setCompletedStages] = useState([]);

  const stages = [
    {
      title: "1. Problem Definition",
      color: "bg-blue-500",
      hoverColor: "hover:bg-blue-600",
      icon: Target,
      items: [
        "Define business/clinical problem",
        "Identify stakeholders",
        "Set objectives and KPIs",
        "Assess feasibility"
      ],
      details: {
        description: "Foundation phase where we define what problem we're solving and why it matters.",
        example: "Predict 30-day hospital readmission with 80% recall to enable targeted interventions",
        challenges: ["Unclear success metrics", "Stakeholder misalignment", "Scope creep"],
        tools: ["CRISP-DM Framework", "Stakeholder Mapping", "SMART Objectives"]
      }
    },
    {
      title: "2. Data Collection",
      color: "bg-green-500",
      hoverColor: "hover:bg-green-600",
      icon: Database,
      items: [
        "Identify data sources",
        "Assess data availability & quality",
        "Legal/ethical review (HIPAA, consent)",
        "Extract and aggregate data"
      ],
      details: {
        description: "Gather data from multiple sources while ensuring compliance and quality.",
        example: "Extract EHR data, administrative records, and clinical notes from hospital systems",
        challenges: ["Missing data", "Data silos", "Privacy regulations", "Legacy system integration"],
        tools: ["SQL", "ETL Pipelines", "Data Quality Tools"]
      }
    },
    {
      title: "3. Data Exploration & Analysis",
      color: "bg-purple-500",
      hoverColor: "hover:bg-purple-600",
      icon: TrendingUp,
      items: [
        "Exploratory Data Analysis (EDA)",
        "Identify patterns and correlations",
        "Detect biases and data quality issues",
        "Statistical summary"
      ],
      details: {
        description: "Understand your data's characteristics, distributions, and potential issues.",
        example: "Discover that 65% of readmissions occur in patients >65 with 3+ comorbidities",
        challenges: ["Hidden correlations", "Class imbalance", "Outliers", "Bias detection"],
        tools: ["Pandas", "Matplotlib", "Seaborn", "Plotly"]
      }
    },
    {
      title: "4. Data Preprocessing",
      color: "bg-yellow-500",
      hoverColor: "hover:bg-yellow-600",
      icon: Settings,
      items: [
        "Handle missing values",
        "Outlier detection and treatment",
        "Feature engineering",
        "Normalization/standardization",
        "Train/validation/test split"
      ],
      details: {
        description: "Clean and transform raw data into model-ready format with meaningful features.",
        example: "Create polypharmacy flag (10+ meds), impute missing labs, standardize age/LOS",
        challenges: ["Clinical validity of imputation", "Feature selection", "Data leakage"],
        tools: ["Scikit-learn", "Feature-engine", "Imbalanced-learn"]
      }
    },
    {
      title: "5. Model Selection",
      color: "bg-red-500",
      hoverColor: "hover:bg-red-600",
      icon: Brain,
      items: [
        "Choose algorithm family",
        "Consider interpretability vs accuracy",
        "Assess computational constraints",
        "Select baseline model"
      ],
      details: {
        description: "Select the most appropriate algorithm balancing performance and interpretability.",
        example: "Choose Logistic Regression over Neural Networks for clinical interpretability",
        challenges: ["Accuracy vs interpretability trade-off", "Resource constraints", "Regulatory requirements"],
        tools: ["Scikit-learn", "XGBoost", "TensorFlow", "PyTorch"]
      }
    },
    {
      title: "6. Model Training",
      color: "bg-indigo-500",
      hoverColor: "hover:bg-indigo-600",
      icon: GitBranch,
      items: [
        "Train on training set",
        "Hyperparameter tuning",
        "Cross-validation",
        "Address overfitting/underfitting",
        "Regularization techniques"
      ],
      details: {
        description: "Train model with optimal parameters while preventing overfitting through validation.",
        example: "GridSearch over C=[0.001-100], use 5-fold CV, apply L2 regularization",
        challenges: ["Overfitting", "Hyperparameter optimization", "Long training times"],
        tools: ["GridSearchCV", "Optuna", "Weights & Biases"]
      }
    },
    {
      title: "7. Model Evaluation",
      color: "bg-pink-500",
      hoverColor: "hover:bg-pink-600",
      icon: CheckCircle,
      items: [
        "Test on held-out test set",
        "Calculate metrics (accuracy, precision, recall, F1, AUROC)",
        "Confusion matrix analysis",
        "Fairness audit (demographic parity)",
        "Error analysis"
      ],
      details: {
        description: "Rigorously evaluate model performance and fairness across all patient groups.",
        example: "Achieved 80% recall, 57% precision, AUROC 0.85, fairness audit shows DI=0.82",
        challenges: ["Metric selection", "Class imbalance", "Detecting bias", "Validation strategy"],
        tools: ["Scikit-learn metrics", "Fairlearn", "AIF360"]
      }
    },
    {
      title: "8. Model Interpretation",
      color: "bg-teal-500",
      hoverColor: "hover:bg-teal-600",
      icon: FileText,
      items: [
        "Feature importance analysis",
        "SHAP/LIME explanations",
        "Clinical validation with experts",
        "Document decision logic"
      ],
      details: {
        description: "Understand and explain how the model makes predictions for trust and compliance.",
        example: "Top factors: previous admissions (0.45), age (0.32), comorbidities (0.28)",
        challenges: ["Complex model interpretability", "Clinician trust", "Regulatory explanation requirements"],
        tools: ["SHAP", "LIME", "ELI5", "InterpretML"]
      }
    },
    {
      title: "9. Deployment",
      color: "bg-orange-500",
      hoverColor: "hover:bg-orange-600",
      icon: Users,
      items: [
        "Integration with existing systems",
        "API development",
        "User interface design",
        "Pilot testing",
        "Staff training",
        "Full rollout"
      ],
      details: {
        description: "Deploy model into production environment with proper integration and training.",
        example: "Flask API → EHR integration → Dashboard display → 2-week pilot → Full rollout",
        challenges: ["System integration", "HIPAA compliance", "User adoption", "Downtime prevention"],
        tools: ["Flask/FastAPI", "Docker", "Kubernetes", "AWS Healthcare"]
      }
    },
    {
      title: "10. Monitoring & Maintenance",
      color: "bg-cyan-500",
      hoverColor: "hover:bg-cyan-600",
      icon: RefreshCw,
      items: [
        "Track performance metrics",
        "Monitor for concept drift",
        "Detect fairness degradation",
        "Collect feedback",
        "Schedule retraining",
        "Continuous improvement"
      ],
      details: {
        description: "Continuously monitor model performance and fairness, retraining as needed.",
        example: "Weekly drift detection, monthly performance review, retrain if F1 drops >5%",
        challenges: ["Concept drift detection", "Performance degradation", "Maintaining fairness"],
        tools: ["Evidently AI", "Prometheus", "Grafana", "MLflow"]
      }
    }
  ];

  const toggleComplete = (index) => {
    if (completedStages.includes(index)) {
      setCompletedStages(completedStages.filter(i => i !== index));
    } else {
      setCompletedStages([...completedStages, index]);
    }
  };

  return (
    <div className="w-full min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="inline-block bg-gradient-to-r from-blue-500 to-purple-500 p-1 rounded-2xl mb-4">
            <div className="bg-slate-900 px-6 py-3 rounded-xl">
              <h1 className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">
                AI Development Workflow
              </h1>
            </div>
          </div>
          <p className="text-xl text-gray-300 mb-2">
            End-to-End Process for Healthcare Predictive Modeling
          </p>
          <p className="text-sm text-gray-400">
            Interactive workflow by <span className="text-blue-400 font-semibold">Happy Igho Umukoro</span>
          </p>
          <p className="text-xs text-gray-500">
            princeigho74@gmail.com | +2348065292102
          </p>
          
          {/* Progress Tracker */}
          <div className="mt-6 bg-slate-800 rounded-lg p-4 max-w-md mx-auto">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-300">Progress</span>
              <span className="text-sm text-blue-400 font-semibold">
                {completedStages.length}/{stages.length} stages
              </span>
            </div>
            <div className="w-full bg-slate-700 rounded-full h-3">
              <div 
                className="bg-gradient-to-r from-blue-500 to-purple-500 h-3 rounded-full transition-all duration-500"
                style={{ width: `${(completedStages.length / stages.length) * 100}%` }}
              />
            </div>
          </div>

          {/* Info Banner */}
          <div className="mt-4 inline-flex items-center gap-2 bg-yellow-900/30 border-2 border-yellow-600 rounded-lg px-4 py-2">
            <AlertTriangle className="text-yellow-400" size={20} />
            <span className="text-sm font-semibold text-yellow-300">
              Click any stage to explore details • Mark stages as complete
            </span>
          </div>
        </div>

        {/* Workflow Stages */}
        <div className="relative">
          {stages.map((stage, index) => {
            const Icon = stage.icon;
            const isSelected = selectedStage === index;
            const isExpanded = expandedStage === index;
            const isCompleted = completedStages.includes(index);
            
            return (
              <div key={index} className="mb-6">
                {/* Stage Card */}
                <div 
                  className={`bg-slate-800 rounded-xl shadow-2xl border-2 ${
                    isSelected ? 'border-purple-500 shadow-purple-500/50' : 'border-slate-700'
                  } overflow-hidden transform transition-all duration-300 ${
                    isSelected ? 'scale-105' : 'hover:scale-102'
                  } cursor-pointer`}
                  onClick={() => {
                    setSelectedStage(isSelected ? null : index);
                    setExpandedStage(isExpanded ? null : index);
                  }}
                >
                  {/* Header */}
                  <div className={`${stage.color} ${stage.hoverColor} text-white p-4 flex items-center justify-between transition-colors`}>
                    <div className="flex items-center gap-3">
                      {isCompleted && (
                        <CheckSquare className="text-green-300" size={24} />
                      )}
                      <Icon size={28} />
                      <h2 className="text-xl font-bold">{stage.title}</h2>
                    </div>
                    <div className="flex items-center gap-2">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          toggleComplete(index);
                        }}
                        className="p-2 bg-white/20 hover:bg-white/30 rounded-lg transition-colors"
                      >
                        {isCompleted ? (
                          <CheckCircle size={20} />
                        ) : (
                          <AlertCircle size={20} />
                        )}
                      </button>
                      <ChevronRight 
                        className={`transform transition-transform ${isExpanded ? 'rotate-90' : ''}`}
                        size={24}
                      />
                    </div>
                  </div>
                  
                  {/* Basic Content */}
                  <div className="p-6 bg-slate-800">
                    <ul className="space-y-2">
                      {stage.items.map((item, itemIndex) => (
                        <li key={itemIndex} className="flex items-start gap-3 text-gray-300 hover:text-white transition-colors">
                          <div className="mt-1.5 w-2 h-2 rounded-full bg-gradient-to-r from-blue-400 to-purple-400 flex-shrink-0"></div>
                          <span>{item}</span>
                        </li>
                      ))}
                    </ul>

                    {/* Expanded Details */}
                    {isExpanded && (
                      <div className="mt-6 space-y-4 animate-fadeIn">
                        <div className="bg-slate-700/50 rounded-lg p-4 border border-slate-600">
                          <h4 className="text-blue-400 font-semibold mb-2 flex items-center gap-2">
                            <Info size={18} />
                            Description
                          </h4>
                          <p className="text-gray-300 text-sm">{stage.details.description}</p>
                        </div>

                        <div className="bg-green-900/20 rounded-lg p-4 border border-green-700">
                          <h4 className="text-green-400 font-semibold mb-2">Example</h4>
                          <p className="text-gray-300 text-sm italic">"{stage.details.example}"</p>
                        </div>

                        <div className="bg-red-900/20 rounded-lg p-4 border border-red-700">
                          <h4 className="text-red-400 font-semibold mb-2">Common Challenges</h4>
                          <ul className="space-y-1">
                            {stage.details.challenges.map((challenge, i) => (
                              <li key={i} className="text-gray-300 text-sm flex items-center gap-2">
                                <X size={14} className="text-red-400" />
                                {challenge}
                              </li>
                            ))}
                          </ul>
                        </div>

                        <div className="bg-purple-900/20 rounded-lg p-4 border border-purple-700">
                          <h4 className="text-purple-400 font-semibold mb-2">Tools & Technologies</h4>
                          <div className="flex flex-wrap gap-2">
                            {stage.details.tools.map((tool, i) => (
                              <span key={i} className="px-3 py-1 bg-purple-700/50 rounded-full text-xs text-purple-200">
                                {tool}
                              </span>
                            ))}
                          </div>
                        </div>
                      </div>
                    )}
                  </div>
                </div>

                {/* Arrow between stages */}
                {index < stages.length - 1 && (
                  <div className="flex justify-center my-4">
                    <div className="flex flex-col items-center">
                      <ArrowDown size={32} className="text-purple-400 animate-bounce" strokeWidth={3} />
                      <span className="text-xs text-gray-500 mt-1">Next Stage</span>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* Feedback Loop Section */}
        <button
          onClick={() => setShowFeedback(!showFeedback)}
          className="w-full mt-8 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white rounded-xl shadow-lg p-6 transition-all duration-300 transform hover:scale-105"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <RefreshCw className="text-white" size={28} />
              <h3 className="text-2xl font-bold">Feedback Loops & Iterations</h3>
            </div>
            <ChevronRight 
              className={`transform transition-transform ${showFeedback ? 'rotate-90' : ''}`}
              size={28}
            />
          </div>
        </button>

        {showFeedback && (
          <div className="mt-4 bg-slate-800 rounded-xl shadow-lg border-2 border-blue-500 p-6 animate-fadeIn">
            <p className="text-gray-300 mb-4">
              AI development is iterative! You may need to loop back to previous stages based on findings:
            </p>
            <div className="grid md:grid-cols-2 gap-4">
              <div className="bg-gradient-to-br from-blue-900/40 to-blue-800/20 p-4 rounded-lg border border-blue-700">
                <p className="font-semibold text-blue-300 mb-2">Evaluation → Preprocessing/Training</p>
                <p className="text-sm text-gray-300">If metrics are poor, revisit feature engineering or try different algorithms</p>
              </div>
              <div className="bg-gradient-to-br from-purple-900/40 to-purple-800/20 p-4 rounded-lg border border-purple-700">
                <p className="font-semibold text-purple-300 mb-2">Monitoring → Data Collection</p>
                <p className="text-sm text-gray-300">Concept drift detected? Collect new data and retrain model</p>
              </div>
              <div className="bg-gradient-to-br from-green-900/40 to-green-800/20 p-4 rounded-lg border border-green-700">
                <p className="font-semibold text-green-300 mb-2">Deployment → Problem Definition</p>
                <p className="text-sm text-gray-300">User feedback may reveal need to reframe objectives</p>
              </div>
              <div className="bg-gradient-to-br from-orange-900/40 to-orange-800/20 p-4 rounded-lg border border-orange-700">
                <p className="font-semibold text-orange-300 mb-2">Interpretation → Model Selection</p>
                <p className="text-sm text-gray-300">If model is too opaque, choose more interpretable approach</p>
              </div>
            </div>
          </div>
        )}

        {/* Key Considerations */}
        <div className="mt-8 bg-gradient-to-br from-slate-800 to-slate-900 rounded-xl shadow-2xl border-2 border-purple-500 p-6">
          <h3 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400 mb-4">
            Critical Considerations Throughout
          </h3>
          <div className="grid md:grid-cols-3 gap-4">
            <div className="bg-slate-700/50 p-4 rounded-lg shadow border border-purple-600 hover:border-purple-400 transition-colors">
              <h4 className="font-bold text-purple-300 mb-2 flex items-center gap-2">
                <AlertTriangle size={18} />
                Ethics & Bias
              </h4>
              <p className="text-sm text-gray-300">Monitor fairness across demographic groups at every stage</p>
            </div>
            <div className="bg-slate-700/50 p-4 rounded-lg shadow border border-blue-600 hover:border-blue-400 transition-colors">
              <h4 className="font-bold text-blue-300 mb-2 flex items-center gap-2">
                <Users size={18} />
                Stakeholder Engagement
              </h4>
              <p className="text-sm text-gray-300">Continuous communication with clinicians and patients</p>
            </div>
            <div className="bg-slate-700/50 p-4 rounded-lg shadow border border-green-600 hover:border-green-400 transition-colors">
              <h4 className="font-bold text-green-300 mb-2 flex items-center gap-2">
                <FileText size={18} />
                Documentation
              </h4>
              <p className="text-sm text-gray-300">Maintain detailed records for compliance and reproducibility</p>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-8 text-center text-sm text-gray-400 space-y-2">
          <p className="italic">Based on CRISP-DM Framework adapted for Healthcare AI Applications</p>
          <p className="font-semibold text-gray-300">Assignment: AI Development Workflow - Hospital Readmission Prediction</p>
          <div className="pt-4 border-t border-slate-700 mt-4">
            <p className="text-blue-400">Developed by Happy Igho Umukoro</p>
            <p className="text-xs text-gray-500">princeigho74@gmail.com | +2348065292102</p>
          </div>
        </div>
      </div>

      <style jsx>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(-10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fadeIn {
          animation: fadeIn 0.3s ease-out;
        }
      `}</style>
    </div>
  );
}

# UPDATED SECTIONS FOR YOUR app.py

# 1. UPDATE THE QUESTIONS DICTIONARY (Replace the existing QUESTIONS section)
QUESTIONS = {
    "sta": [
        "What is Static Timing Analysis (STA)? Why is it important in chip design?",
        "Explain setup time and hold time. What happens when these requirements are violated?",
        "What is slack? How do you calculate setup slack and hold slack?",
        "Your design has setup violations of -30ps. List 3 methods to fix these violations.",
        "What is clock skew? How does it affect setup and hold timing?",
        "Explain timing corners. Which corners do you use for setup and hold analysis?",
        "What are timing exceptions? When would you use false paths?",
        "Describe the difference between ideal clock and propagated clock analysis.",
        "What is clock jitter? How do you account for it in timing calculations?",
        "Your hold violations are at 25ps. What are the common ways to fix hold violations?",
        "What is OCV (On-Chip Variation)? Why do you add OCV margins in STA?",
        "Explain multicycle paths. Give an example where you would use them.",
        "How do you analyze timing for multiple clock domains?",
        "What is clock domain crossing (CDC)? What timing checks are needed?",
        "Describe timing analysis for memory interfaces (SRAM). What makes it different?",
        "What reports do you check for timing signoff? List the key timing reports.",
        "How do you handle timing analysis for generated clocks?",
        "What is timing correlation? How do you ensure STA matches real silicon performance?"
    ],
    
    "cts": [
        "What is Clock Tree Synthesis (CTS)? Why do we build clock trees?",
        "What is clock skew? What is an acceptable skew target for most designs?",
        "Explain clock insertion delay. How is it different from clock skew?",
        "Your clock tree has 150ps skew but target is 50ps. How would you reduce it?",
        "What elements are used to build clock trees? Describe buffers and inverters.",
        "What is clock tree balancing? How do you achieve balanced insertion delay?",
        "What is useful skew? Give an example where you would use it intentionally.",
        "How do clock gating cells affect your clock tree? Where do you place them?",
        "Compare H-tree vs balanced tree topologies. When would you use each?",
        "Your design has 3 clock domains. How do you handle multiple clocks in CTS?",
        "What techniques can you use to reduce clock tree power consumption?",
        "How do you build clock trees when you have multiple voltage domains?",
        "What is clock mesh? When would you choose mesh over tree topology?",
        "Describe CTS challenges for high-frequency designs (>1GHz).",
        "How do you handle CTS for designs with power gating?",
        "What is the typical flow sequence? When does CTS happen relative to placement and routing?",
        "How do you optimize clock trees for process variation and yield?",
        "What reports do you check after CTS? How do you verify clock tree quality?"
    ],
    
    "signoff": [
        "What is signoff in chip design? What must pass before tape-out?",
        "List 5 major signoff checks. Why is each one important?",
        "What is DRC (Design Rule Check)? Give 3 examples of common DRC violations.",
        "What is LVS (Layout vs Schematic)? What does an LVS mismatch mean?",
        "Your design has 20 LVS errors. What systematic approach would you use to debug them?",
        "What is antenna checking? Why can antenna violations damage your chip?",
        "Explain metal density rules. What happens if density is too low?",
        "What is IR drop analysis? What are typical IR drop limits?",
        "Your design has IR drop violations of 120mV. How would you fix them?",
        "What is electromigration (EM)? How do you prevent EM violations?",
        "Describe timing signoff. What timing reports are required?",
        "What is signal integrity (SI) analysis? What SI effects do you check?",
        "How do you perform power analysis for signoff? What power metrics matter?",
        "What additional checks are needed for multi-voltage designs?",
        "What is formal verification? How is it different from simulation?",
        "Explain thermal analysis. How do you ensure your chip won't overheat?",
        "What is yield analysis? How do you optimize for manufacturing yield?",
        "Describe the typical signoff flow. Who signs off on what?"
    ],
    
    "synthesis": [
        "What is RTL synthesis? Explain the process of converting RTL to gate-level netlist.",
        "What are synthesis constraints? List the main types of constraints used in synthesis.",
        "Explain the difference between combinational and sequential optimization in synthesis.",
        "Your design fails timing after synthesis. List 5 techniques to improve timing closure.",
        "What is area optimization? How do you balance area vs timing vs power?",
        "Describe the synthesis flow. What are the key steps from RTL to netlist?",
        "What is technology mapping? How does the tool choose which gates to use?",
        "Explain clock gating. How does synthesis implement clock gating for power reduction?",
        "What is retiming? When would you use retiming optimization?",
        "Your design has high leakage power. What synthesis techniques reduce leakage?",
        "What are multi-Vt libraries? How do you use different threshold voltage cells?",
        "Describe synthesis for low power design. What are the key power optimization techniques?",
        "What is hierarchical synthesis? When do you use flat vs hierarchical synthesis?",
        "How do you handle memories and IP blocks during synthesis?",
        "What is the difference between compile and compile_ultra in Design Compiler?",
        "Explain synthesis optimization priorities. How do you set timing vs area vs power goals?",
        "What synthesis reports do you check for quality? How do you analyze QoR?",
        "How do you prepare synthesis scripts for different process corners and modes?"
    ],
    
    # NEW DFT SUB-TOPICS
    "dft_scan": [  # For Shama - Scan Chain & ATPG Specialist (15 questions)
        "What is scan chain methodology? Explain the basic principle of scan testing.",
        "Describe the scan cell structure. How does a scan flip-flop differ from a normal flip-flop?",
        "What are the different types of scan architectures? Compare muxed-D vs clocked scan.",
        "Explain scan chain stitching process. What factors determine the scan chain order?",
        "Your design has 50,000 flip-flops. How would you determine the optimal number of scan chains?",
        "What is scan compression? Explain EDT (Embedded Deterministic Test) technique.",
        "Describe ATPG (Automatic Test Pattern Generation). What are the main ATPG algorithms?",
        "What is stuck-at fault model? Explain single stuck-at-0 and stuck-at-1 faults.",
        "Describe transition delay fault model. When would you use it over stuck-at?",
        "Your scan chains have timing violations. What are the common causes and solutions?",
        "What is X-tolerance in ATPG? How do you handle unknown states in scan testing?",
        "Explain scan enable signal routing. What timing constraints apply to scan enable?",
        "What is launch-on-capture vs launch-on-shift in transition delay testing?",
        "How do you handle scan testing in multi-voltage domains? What are the challenges?",
        "Your fault coverage is 85%. List 5 techniques to improve fault coverage to 95%."
    ],
    
    "dft_bist": [  # For Anbu - Built-In Self Test Specialist (15 questions)
        "What is MBIST (Memory Built-In Self Test)? Why is it essential for memory testing?",
        "Describe the MBIST architecture. What are the key components of an MBIST controller?",
        "What are March algorithms in memory testing? Explain March C- algorithm.",
        "Your SRAM has MBIST failures. How would you debug and localize the failing memory locations?",
        "What is LBIST (Logic Built-In Self Test)? Compare LBIST vs external scan testing.",
        "Explain PRPG (Pseudo-Random Pattern Generator) in LBIST. What are LFSR-based patterns?",
        "What is MISR (Multiple Input Signature Register)? How does signature analysis work?",
        "Describe collar-based MBIST vs embedded MBIST approaches. When to use each?",
        "What are the different memory fault models? Explain stuck-at, coupling, and data retention faults.",
        "How do you implement MBIST for different memory types (SRAM, ROM, CAM, FIFO)?",
        "What is BIRA (Built-In Redundancy Analysis)? How does it work with MBIST?",
        "Explain MBIST scheduling and power management. How do you sequence multiple MBIST controllers?",
        "What are the challenges of MBIST in low-power designs? How do you handle power gating?",
        "Describe MBIST collar design. What signals are required in the MBIST interface?",
        "How do you verify MBIST functionality? What are the key verification checks?"
    ],
    
    "dft_boundary": [  # For Kiran - Boundary Scan & Advanced DFT Specialist (15 questions)
        "What is JTAG boundary scan? Explain the IEEE 1149.1 standard.",
        "Describe the JTAG architecture. What are the key components of a JTAG TAP controller?",
        "What are the JTAG instructions? Explain BYPASS, SAMPLE, EXTEST, and INTEST.",
        "How do you implement boundary scan in a multi-chip system? What is boundary scan chaining?",
        "Your JTAG chain is broken. What systematic approach would you use to debug it?",
        "What is IEEE 1149.6 for AC-coupled signals? When and why would you use it?",
        "Explain JTAG-based in-system programming (ISP). How does it work for FPGA/Flash programming?",
        "What are the DFT challenges in mixed-signal designs? How do you test analog blocks?",
        "Describe clock domain crossing (CDC) issues in DFT. How do you handle multiple clock domains?",
        "What is hierarchical DFT? How do you implement DFT in a core-based design methodology?",
        "Explain DFT for security-critical designs. What are the security vs testability trade-offs?",
        "What is functional safety in DFT (ISO 26262)? How do you implement safety-compliant test structures?",
        "Describe advanced DFT techniques: parallel testing, broadcast scan, and adaptive scan.",
        "How do you implement DFT for 3D-IC and through-silicon-via (TSV) based designs?",
        "What are the emerging trends in DFT? Explain machine learning applications in test and diagnosis."
    ]
}

# 2. UPDATE THE SCORING CRITERIA (Add to analyze_answer_quality function)
scoring_criteria = {
    'sta': {
        'excellent_terms': ['setup time', 'hold time', 'slack', 'timing violation', 'clock skew', 'timing corner', 'propagated clock', 'jitter', 'ocv'],
        'good_terms': ['timing', 'clock', 'delay', 'path', 'constraint', 'analysis', 'signoff', 'violation'],
        'methodology_terms': ['systematic', 'approach', 'method', 'technique', 'optimization', 'analysis']
    },
    'cts': {
        'excellent_terms': ['clock tree', 'skew', 'insertion delay', 'balancing', 'useful skew', 'clock gating', 'h-tree', 'clock mesh', 'power optimization'],
        'good_terms': ['clock', 'tree', 'buffer', 'delay', 'synthesis', 'distribution', 'domain', 'topology'],
        'methodology_terms': ['optimization', 'technique', 'approach', 'method', 'strategy', 'implementation']
    },
    'signoff': {
        'excellent_terms': ['drc', 'lvs', 'antenna', 'ir drop', 'electromigration', 'metal density', 'signal integrity', 'formal verification'],
        'good_terms': ['signoff', 'verification', 'check', 'violation', 'analysis', 'tape-out', 'design rule'],
        'methodology_terms': ['systematic', 'debug', 'approach', 'method', 'flow', 'process']
    },
    'synthesis': {
        'excellent_terms': ['rtl synthesis', 'technology mapping', 'retiming', 'clock gating', 'multi-vt', 'hierarchical', 'compile_ultra', 'qor', 'optimization'],
        'good_terms': ['synthesis', 'netlist', 'constraint', 'timing', 'area', 'power', 'optimization', 'gate', 'library'],
        'methodology_terms': ['systematic', 'approach', 'method', 'technique', 'flow', 'strategy']
    },
    'dft_scan': {
        'excellent_terms': ['scan chain', 'atpg', 'scan flip-flop', 'scan compression', 'edt', 'stuck-at', 'transition delay', 'fault coverage', 'x-tolerance'],
        'good_terms': ['scan', 'test', 'fault', 'pattern', 'coverage', 'stitching', 'enable', 'capture', 'shift'],
        'methodology_terms': ['systematic', 'approach', 'method', 'technique', 'optimization', 'analysis']
    },
    'dft_bist': {
        'excellent_terms': ['mbist', 'lbist', 'march algorithm', 'prpg', 'misr', 'bira', 'signature analysis', 'memory fault', 'lfsr'],
        'good_terms': ['bist', 'memory', 'test', 'built-in', 'controller', 'pattern', 'signature', 'collar', 'sram'],
        'methodology_terms': ['systematic', 'approach', 'method', 'technique', 'scheduling', 'verification']
    },
    'dft_boundary': {
        'excellent_terms': ['jtag', 'boundary scan', 'ieee 1149', 'tap controller', 'extest', 'intest', 'bypass', 'hierarchical dft', 'mixed-signal'],
        'good_terms': ['boundary', 'scan', 'jtag', 'test', 'chain', 'instruction', 'debug', 'programming', 'security'],
        'methodology_terms': ['systematic', 'approach', 'method', 'technique', 'implementation', 'verification']
    }
}

# 3. UPDATE THE ADMIN DROPDOWN (Replace the topic selection in admin route)
# In the admin route, update the select options to:
"""
<option value="sta">STA (Static Timing Analysis)</option>
<option value="cts">CTS (Clock Tree Synthesis)</option>
<option value="signoff">Signoff Checks</option>
<option value="synthesis">Synthesis</option>
<option value="dft_scan">DFT - Scan & ATPG (Shama)</option>
<option value="dft_bist">DFT - BIST & Memory Test (Anbu)</option>
<option value="dft_boundary">DFT - Boundary Scan & Advanced (Kiran)</option>
"""

# 4. UPDATE ENGINEER ASSIGNMENTS (Optional - for specific assignments)
# You can modify the create_test function to auto-assign DFT specialists:
def auto_assign_dft_specialist(topic):
    """Auto-assign DFT topics to specialists"""
    dft_assignments = {
        'dft_scan': 'eng020',      # Shama
        'dft_bist': 'eng019',      # Anbu  
        'dft_boundary': 'eng021'   # Kiran
    }
    return dft_assignments.get(topic, None)

# 5. UPDATE SYSTEM OVERVIEW STATS
# Change "90 Questions total" to "105 Questions total" in admin dashboard
# (18 STA + 18 CTS + 18 Signoff + 18 Synthesis + 15×3 DFT = 105 total)


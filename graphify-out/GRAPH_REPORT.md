# Graph Report - object-oriented-design-principles  (2026-10-22)

## Corpus Check
- Corpus is ~13,288 words - fits in a single context window. You may not need a graph.

## Summary
- 318 nodes · 466 edges · 22 communities (10 shown, 12 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 31 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Printer ISP After
- Printer ISP Before
- Dependency Inversion Catalog
- Project Docs and AI Context
- Test Suite and Docs Sync
- Student OCP After
- Employee SRP Example
- Product Substitution After
- Product Factory Pattern
- ISP Concept Notes
- Employee SRP Before
- Product Substitution Before
- Student OCP Before
- Docs Sync Hook
- Dependency Inversion Before
- Python Rules Doc
- Project Root

## God Nodes (most connected - your core abstractions)
1. `StudentProfile` - 13 edges
2. `ProductCatalog` - 12 edges
3. `Multifunction` - 12 edges
4. `Dependency Inversion README (D)` - 12 edges
5. `XeroxWorkCentre` - 11 edges
6. `Employee` - 11 edges
7. `PATTERNS.md — Guía de patrones SOLID` - 11 edges
8. `ProductRepository` - 10 edges
9. `Container` - 10 edges
10. `configure_container()` - 10 edges

## Surprising Connections (you probably didn't know these)
- `knows (ambiguous AST entity, before SRP)` --conceptually_related_to--> `Employee`  [AMBIGUOUS]
  .codesight/CODESIGHT.md → single_responsibility/employee_example_before_single_responsibility.py
- `Cohesion` --semantically_similar_to--> `Single Responsibility README (S)`  [INFERRED] [semantically similar]
  README.md → single_responsibility/README.md
- `Coupling` --semantically_similar_to--> `Dependency Inversion README (D)`  [INFERRED] [semantically similar]
  README.md → dependency_inversion/README.md
- `Coupling` --semantically_similar_to--> `Single Responsibility README (S)`  [INFERRED] [semantically similar]
  README.md → single_responsibility/README.md
- `Dependency Inversion README (D)` --references--> `ProductCatalog`  [EXTRACTED]
  dependency_inversion/README.md → dependency_inversion/product_catalog_before_dependency_inversion.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Classes implementing the segregated Print/Scan/Fax interfaces** — interface_segregation_printer_example_with_interface_segregation_print, interface_segregation_printer_example_with_interface_segregation_scan, interface_segregation_printer_example_with_interface_segregation_fax, interface_segregation_printer_example_with_interface_segregation_xeroxworkcentre, interface_segregation_printer_example_with_interface_segregation_hpprinterscanner, interface_segregation_printer_example_with_interface_segregation_cannonprinter [EXTRACTED 1.00]
- **StudentProfile and its implementing student types** — open_close_student_example_with_open_close_studentprofile, open_close_student_example_with_open_close_universitystudent, open_close_student_example_with_open_close_highschoolstudent, open_close_student_example_with_open_close_elementaryschoolstudent [EXTRACTED 1.00]
- **The five SOLID principles** — patterns_single_responsibility_principle, patterns_open_closed_principle, patterns_liskov_substitution_principle, patterns_interface_segregation_principle, patterns_dependency_inversion_principle [EXTRACTED 1.00]

## Communities (22 total, 12 thin omitted)

### Community 0 - "Printer ISP After"
Cohesion: 0.07
Nodes (9): CannonPrinter, Fax, HPPrinterScanner, Print, Scan, XeroxWorkCentre, test_client_depends_only_on_the_capability_it_needs(), scan_document() (+1 more)

### Community 1 - "Printer ISP Before"
Cohesion: 0.06
Nodes (3): CannonPrinter, HPPrinterScanner, Multifunction

### Community 2 - "Dependency Inversion Catalog"
Cohesion: 0.12
Nodes (11): ecommerce_main_application(), ProductCatalog, ProductRepository, SQLProductRepository, configure_container(), Container, ecommerce_main_application(), InMemoryProductRepository (+3 more)

### Community 3 - "Project Docs and AI Context"
Cohesion: 0.10
Nodes (28): .claude/testing.md — Testing and Validation Rules, CODESIGHT.md — AI Context Map, .codesight/graph.md — Dependency Graph, .codesight/libs.md — Libraries, Wiki index.md, Wiki libraries.md, Wiki log.md, Wiki overview.md (+20 more)

### Community 4 - "Test Suite and Docs Sync"
Cohesion: 0.15
Nodes (8): _public_classes(), _read(), test_example_classes_are_documented(), test_example_is_linked_in_its_readme(), test_example_is_linked_in_the_main_readme(), test_patterns_templates_do_not_shadow_builtins(), test_example_runs(), test_snippet_runs()

### Community 5 - "Student OCP After"
Cohesion: 0.12
Nodes (8): DiscountCalculator, ElementarySchoolStudent, HighSchoolStudent, StudentProfile, UniversityStudent, FullFeeStudent, ScholarshipStudent, test_new_profiles_work_without_modifying_the_calculator()

### Community 6 - "Employee SRP Example"
Cohesion: 0.17
Nodes (7): Employee, EmployeeRepository, TaxCalculator, employee(), test_employee_only_holds_data(), test_repository_saves_employee(), test_tax_calculator_depends_on_employee_type()

### Community 7 - "Product Substitution After"
Cohesion: 0.23
Nodes (6): client(), InCommerceProduct, InHouseProduct, Product, test_every_subtype_substitutes_product(), test_get_discount_has_no_side_effects()

### Community 8 - "Product Factory Pattern"
Cohesion: 0.18
Nodes (4): ProductCatalog, ProductFactory, ProductRepository, SQLProductRepository

### Community 11 - "Product Substitution Before"
Cohesion: 0.23
Nodes (4): client(), InCommerceProduct, InHouseProduct, Product

## Ambiguous Edges - Review These
- `Employee` → `knows (ambiguous AST entity, before SRP)`  [AMBIGUOUS]
  .codesight/CODESIGHT.md · relation: conceptually_related_to

## Knowledge Gaps
- **16 isolated node(s):** `object-oriented-design-principles`, `.claude/python.md — Python Rules`, `knows (ambiguous AST entity, before SRP)`, `.codesight/graph.md — Dependency Graph`, `.codesight/libs.md — Libraries` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 141 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Interface Segregation README (I)` connect `Project Docs and AI Context` to `Printer ISP After`, `Printer ISP Before`?**
  _High betweenness centrality (0.346) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `ProductCatalog` (e.g. with `ecommerce_main_application()` and `test_default_container_uses_sql_repository()`) actually correct?**
  _`ProductCatalog` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `object-oriented-design-principles`, `.claude/python.md — Python Rules`, `knows (ambiguous AST entity, before SRP)` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Printer ISP After` be split into smaller, more focused modules?**
  _Cohesion score 0.06553911205073996 - nodes in this community are weakly interconnected._
- **Why does `Multifunction` connect `Printer ISP Before` to `ISP Concept Notes`, `Project Docs and AI Context`?**
  _High betweenness centrality (0.276) - this node is a cross-community bridge._
- **Should `Printer ISP Before` be split into smaller, more focused modules?**
  _Cohesion score 0.05689900426742532 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Employee` and `knows (ambiguous AST entity, before SRP)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
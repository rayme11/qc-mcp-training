# qc-mcp-training

## Goal
This training is designed to help senior SDETs and automation engineers master MCP concepts and workflows for Quality Control (QC) in API/UI testing. You will learn how to:
- Retrieve and analyze requirements from Jira
- Extract and validate API contracts
- Review existing test coverage
- Design, review, and document test cases
- Automate test case creation and handoff
- Follow secure, maintainable, and standards-compliant practices

All steps are broken down for easy, step-by-step execution. Scripts and guides are provided for each phase, and output is organized in the `out/` folder for traceability.

---


**Pre-requisites**
- GitHub Copilot enabled in IDE
- MCPs configured: Atlassian MCP (Jira), Xray MCP, Git MCP (OpenAPI specs), Playwright MCP
- Project-specific instructions in docs/copilot-instructions.md

**Additional Guides:**
- [Jira Access Setup](docs/jira_access_setup.md)
- [Jira MCP Prompts](docs/jira_mcp_prompts.md)
- [Fetch Jira Requirements](docs/fetch_jira_requirements.md)
- [Secure Development Practices](docs/secure_development_practices.md)

**Reading:**
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [MCP Overview](https://kwri.atlassian.net/wiki/spaces/SAGA/pages/1813774338)

---

# Output & Organization
# - All output files (e.g., requirements_output.txt) should be saved in the `out/` folder. Scripts will create this folder automatically if it does not exist.
# - Scripts accept parameters (e.g., Jira key) for step-by-step verification and easier testing.
## 1. Requirements Analysis (Jira MCP)
**Concept:** Fetch and analyze requirements from Jira using Atlassian MCP.

**Steps:**
- Retrieve requirements (summary, description, acceptance criteria, API endpoints) using the parameterized script.
- Save output to the `out/` folder for each run.
- Analyze for involved endpoints, business rules, validation, auth, dependencies.
- Verify each step by running the script with a specific Jira key and checking the output file.

**Reading:**
- [Jira REST API Guide](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Xray for Jira Documentation](https://docs.getxray.app/display/XRAYCLOUD/Getting+Started)

**Checklist for Step 1:**
- [ ] Jira access configured (API token, permissions)
- [ ] Requirements fetched for relevant project/epic/feature using parameterized script
- [ ] Output saved in `out/` folder
- [ ] Acceptance criteria, endpoints, business rules extracted
- [ ] Summary document/table created for reference

---

## 2. Fetch Existing API Documentation (Git MCP)
**Concept:** Use Git MCP to extract OpenAPI specs and understand API contracts.

**Steps:**
- Locate yaml/spec files for endpoints.
- Extract URLs, methods, schemas, validation, error codes, auth.

**Reading:**
- [OpenAPI Specification](https://swagger.io/specification/)
- [Python OpenAPI Tools](https://github.com/pypa/openapi-python-client)

---

## 3. Check Existing Test Coverage (Git MCP)
**Concept:** Review existing API tests to avoid duplication and identify gaps.

**Steps:**
- Search for test files related to endpoints/services/features.
- List covered cases, test data, helper methods.
- Perform gap analysis.

**Reading:**
- [pytest Documentation](https://docs.pytest.org/en/latest/)
- [Playwright Python Docs](https://playwright.dev/python/docs/intro)

---

## 4. Create Test Design Document
**Concept:** Design comprehensive test cases before implementation.

**Steps:**
- Use templates to document test cases (steps, data, expected results, priorities).

**Reading:**
- [Test Design Template Example](https://kwri.atlassian.net/wiki/spaces/SAGA/pages/1813774338)
- [Xray Test Case Format](https://docs.getxray.app/display/XRAYCLOUD/Test+Case+Specification)

---

## 5. Design Review & Validation
**Concept:** Review test design for completeness, quality, compliance.

**Steps:**
- Coverage check (acceptance criteria, contract rules, scenarios).
- Quality check (clarity, data, results, redundancy).
- Compliance check (standards, naming, structure).
- Generate review report and traceability matrix.

**Reading:**
- [Test Design Review Checklist](https://kwri.atlassian.net/wiki/spaces/SAGA/pages/1813774338)
- [Traceability Matrix Guide](https://www.guru99.com/traceability-matrix.html)

---

## 6. Peer Review Preparation (Human Validation)
**Concept:** Prepare test design for team review.

**Steps:**
- Summarize coverage, checklist, artifacts, questions for reviewers.

**Reading:**
- [Peer Review Best Practices](https://www.atlassian.com/agile/code-reviews)
- [Xray Review Process](https://docs.getxray.app/display/XRAYCLOUD/Reviewing+Test+Cases)

---

## 7. Create Xray Test Cases
**Concept:** Create test cases in Jira/Xray from the design document.

**Steps:**
- Bulk create test cases, link to requirements, return Xray keys.

**Reading:**
- [Xray API for Test Case Creation](https://docs.getxray.app/display/XRAYCLOUD/REST+API)
- [Jira/Xray Integration Guide](https://docs.getxray.app/display/XRAYCLOUD/Jira+Integration)

---

## 8. Design Handoff Documentation (Optional)
**Concept:** Prepare implementation guide for developers/automation engineers.

**Steps:**
- Document endpoints, auth, data, helpers, framework, assertions, execution order, environment setup, special considerations, reference tests, definition of done.

**Reading:**
- [API Test Implementation Guide](https://kwri.atlassian.net/wiki/spaces/SAGA/pages/1813774338)
- [Python REST API Testing with pytest](https://realpython.com/api-integration-in-python/)

---

**Quick Reference: Essential QC Prompts**
- Requirements Analysis: Retrieve and analyze Jira requirements.
- Gap Analysis: Compare requirements with existing tests and OpenAPI spec.
- Test Design: Create detailed test cases.
- Design Review: Check coverage, quality, compliance.
- Xray Test Case: Create Xray test cases from design.
- Implementation Handoff: Generate implementation guide.

---

**Related Reading & Material**
- [Guide: API Test Development with GitHub Copilot (Git & Xray MCPs)](https://kwri.atlassian.net/wiki/spaces/SAGA/pages/1813774338)
- [GitHub Copilot Setup Guide for QA Automation projects with MCP Integrations](https://docs.github.com/en/copilot)
- [MCPs Configuration for GitHub Copilot](https://docs.github.com/en/copilot/configuration)
- [API test case creation guide for Manual QC Engineers via IntelliJ IDEA](https://kwri.atlassian.net/wiki/spaces/SAGA/pages/1813774338)
- [GitHub Copilot Instructions Examples](https://docs.github.com/en/copilot/prompts)
- [GitHub Copilot: Instructions & Prompts Best Practices](https://docs.github.com/en/copilot/best-practices)

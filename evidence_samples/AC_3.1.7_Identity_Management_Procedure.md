# IDENTITY LIFECYCLE MANAGEMENT PROCEDURE
## TechDefense Solutions LLC
### Document: PROC-IAM-001 | Version: 1.3

## Username Creation Standard
Format: [first initial][lastname].[department]
Example: jsmith.eng

## Identifier Reuse Prevention

### Archive Process
1. User termination initiated in HR system
2. Account disabled immediately 
3. Account moved to "Archived Users" OU
4. Retention period: 2 years minimum
5. Username added to "reserved list" permanently

### Reserved Username List (Sample)
| Username | Termination Date | Eligible for Reuse | Status |
|----------|-----------------|-------------------|---------|
| mwilson.eng | 2022-03-15 | 2024-03-15 | Reserved - Never Reuse |
| sjones.hr | 2022-07-20 | 2024-07-20 | Reserved - Never Reuse |
| ksmith.admin | 2023-01-10 | 2025-01-10 | Reserved - Never Reuse |
| rlee.finance | 2023-06-05 | 2025-06-05 | Reserved - Never Reuse |

### Collision Handling
If name collision occurs: append incremental number
- jsmith.eng (original)
- jsmith2.eng (second John Smith in Engineering)
- jsmith3.eng (third John Smith in Engineering)

Total Archived Identities: 347
Policy Violations Since Implementation: 0

_Approved by: IT Director_
_Last Audit: 2024-08-15_

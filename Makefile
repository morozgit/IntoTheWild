start:
	@cd backend && uvicorn src.main:app --reload &
	@echo "Backend started"
	@cd frontend && npm run serve &
	@echo "Frontend started"

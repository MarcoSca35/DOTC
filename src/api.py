"""Defines API."""

from fastapi import APIRouter
from games.endpoints import games_router
from play.endpoints import play_router


api_router = APIRouter()
api_router.include_router(games_router, prefix="/games", tags=["games"])
api_router.include_router(play_router, prefix="/play", tags=["play"])

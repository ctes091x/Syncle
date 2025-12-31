# backend/app/modules/task/models.py

import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Task(Base):
    """
    【Taskテーブル定義】
    タスクの基本情報を管理します。
    MySQLのテーブル定義と一致させる必要があります。
    """

    __tablename__ = "tasks"

    task_id = Column(String(36), primary_key=True,  default=lambda: str(uuid.uuid4()), index=True)

    group_id = Column(String(36), ForeignKey("groups.group_id", ondelete="CASCADE"), nullable=False)

    assigned_to = Column(String(36), ForeignKey("users.user_id"))

    title = Column(String(255), nullable=False)

    date = Column(DateTime, nullable=False)

    time_span_begin = Column(DateTime)

    time_span_end = Column(DateTime)

    place = Column(String(255), )

    description = Column(String(255))

    status = Column(String(255))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    group = relationship("Group", back_populates="tasks", cascade="all, delete-orphan")

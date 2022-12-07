from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_task_creation = lazy_import('msgraph.generated.models.planner_task_creation')

class PlannerTeamsPublicationInfo(planner_task_creation.PlannerTaskCreation):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTeamsPublicationInfo and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerTeamsPublicationInfo"
        # The date and time when this task was last modified by the publication process. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The identifier of the publication. Read-only.
        self._publication_id: Optional[str] = None
        # The identifier of the plannerPlan this task was originally placed in. Read-only.
        self._published_to_plan_id: Optional[str] = None
        # The identifier of the team that initiated the publication process. Read-only.
        self._publishing_team_id: Optional[str] = None
        # The display name of the team that initiated the publication process. This display name is for reference only, and might not represent the most up-to-date name of the team. Read-only.
        self._publishing_team_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTeamsPublicationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTeamsPublicationInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTeamsPublicationInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publication_id": lambda n : setattr(self, 'publication_id', n.get_str_value()),
            "published_to_plan_id": lambda n : setattr(self, 'published_to_plan_id', n.get_str_value()),
            "publishing_team_id": lambda n : setattr(self, 'publishing_team_id', n.get_str_value()),
            "publishing_team_name": lambda n : setattr(self, 'publishing_team_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time when this task was last modified by the publication process. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when this task was last modified by the publication process. Read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def publication_id(self,) -> Optional[str]:
        """
        Gets the publicationId property value. The identifier of the publication. Read-only.
        Returns: Optional[str]
        """
        return self._publication_id
    
    @publication_id.setter
    def publication_id(self,value: Optional[str] = None) -> None:
        """
        Sets the publicationId property value. The identifier of the publication. Read-only.
        Args:
            value: Value to set for the publicationId property.
        """
        self._publication_id = value
    
    @property
    def published_to_plan_id(self,) -> Optional[str]:
        """
        Gets the publishedToPlanId property value. The identifier of the plannerPlan this task was originally placed in. Read-only.
        Returns: Optional[str]
        """
        return self._published_to_plan_id
    
    @published_to_plan_id.setter
    def published_to_plan_id(self,value: Optional[str] = None) -> None:
        """
        Sets the publishedToPlanId property value. The identifier of the plannerPlan this task was originally placed in. Read-only.
        Args:
            value: Value to set for the publishedToPlanId property.
        """
        self._published_to_plan_id = value
    
    @property
    def publishing_team_id(self,) -> Optional[str]:
        """
        Gets the publishingTeamId property value. The identifier of the team that initiated the publication process. Read-only.
        Returns: Optional[str]
        """
        return self._publishing_team_id
    
    @publishing_team_id.setter
    def publishing_team_id(self,value: Optional[str] = None) -> None:
        """
        Sets the publishingTeamId property value. The identifier of the team that initiated the publication process. Read-only.
        Args:
            value: Value to set for the publishingTeamId property.
        """
        self._publishing_team_id = value
    
    @property
    def publishing_team_name(self,) -> Optional[str]:
        """
        Gets the publishingTeamName property value. The display name of the team that initiated the publication process. This display name is for reference only, and might not represent the most up-to-date name of the team. Read-only.
        Returns: Optional[str]
        """
        return self._publishing_team_name
    
    @publishing_team_name.setter
    def publishing_team_name(self,value: Optional[str] = None) -> None:
        """
        Sets the publishingTeamName property value. The display name of the team that initiated the publication process. This display name is for reference only, and might not represent the most up-to-date name of the team. Read-only.
        Args:
            value: Value to set for the publishingTeamName property.
        """
        self._publishing_team_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("publicationId", self.publication_id)
        writer.write_str_value("publishedToPlanId", self.published_to_plan_id)
        writer.write_str_value("publishingTeamId", self.publishing_team_id)
        writer.write_str_value("publishingTeamName", self.publishing_team_name)
    


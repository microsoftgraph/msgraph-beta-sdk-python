from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_creation_source_kind = lazy_import('msgraph.generated.models.planner_creation_source_kind')
planner_teams_publication_info = lazy_import('msgraph.generated.models.planner_teams_publication_info')

class PlannerTaskCreation(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTaskCreation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies what kind of creation source the task is created with. The possible values are: external, publication and unknownFutureValue.
        self._creation_source_kind: Optional[planner_creation_source_kind.PlannerCreationSourceKind] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Information about the publication process that created this task. This field is deprecated and clients should move to using the new inheritance model.
        self._teams_publication_info: Optional[planner_teams_publication_info.PlannerTeamsPublicationInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskCreation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskCreation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskCreation()
    
    @property
    def creation_source_kind(self,) -> Optional[planner_creation_source_kind.PlannerCreationSourceKind]:
        """
        Gets the creationSourceKind property value. Specifies what kind of creation source the task is created with. The possible values are: external, publication and unknownFutureValue.
        Returns: Optional[planner_creation_source_kind.PlannerCreationSourceKind]
        """
        return self._creation_source_kind
    
    @creation_source_kind.setter
    def creation_source_kind(self,value: Optional[planner_creation_source_kind.PlannerCreationSourceKind] = None) -> None:
        """
        Sets the creationSourceKind property value. Specifies what kind of creation source the task is created with. The possible values are: external, publication and unknownFutureValue.
        Args:
            value: Value to set for the creationSourceKind property.
        """
        self._creation_source_kind = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "creation_source_kind": lambda n : setattr(self, 'creation_source_kind', n.get_enum_value(planner_creation_source_kind.PlannerCreationSourceKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "teams_publication_info": lambda n : setattr(self, 'teams_publication_info', n.get_object_value(planner_teams_publication_info.PlannerTeamsPublicationInfo)),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("creationSourceKind", self.creation_source_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("teamsPublicationInfo", self.teams_publication_info)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def teams_publication_info(self,) -> Optional[planner_teams_publication_info.PlannerTeamsPublicationInfo]:
        """
        Gets the teamsPublicationInfo property value. Information about the publication process that created this task. This field is deprecated and clients should move to using the new inheritance model.
        Returns: Optional[planner_teams_publication_info.PlannerTeamsPublicationInfo]
        """
        return self._teams_publication_info
    
    @teams_publication_info.setter
    def teams_publication_info(self,value: Optional[planner_teams_publication_info.PlannerTeamsPublicationInfo] = None) -> None:
        """
        Sets the teamsPublicationInfo property value. Information about the publication process that created this task. This field is deprecated and clients should move to using the new inheritance model.
        Args:
            value: Value to set for the teamsPublicationInfo property.
        """
        self._teams_publication_info = value
    


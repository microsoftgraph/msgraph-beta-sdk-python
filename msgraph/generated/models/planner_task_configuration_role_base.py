from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_relationship_based_user_type, planner_user_role_kind

class PlannerTaskConfigurationRoleBase(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTaskConfigurationRoleBase and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The roleKind property
        self._role_kind: Optional[planner_user_role_kind.PlannerUserRoleKind] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskConfigurationRoleBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskConfigurationRoleBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.plannerRelationshipBasedUserType":
                from . import planner_relationship_based_user_type

                return planner_relationship_based_user_type.PlannerRelationshipBasedUserType()
        return PlannerTaskConfigurationRoleBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_relationship_based_user_type, planner_user_role_kind

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roleKind": lambda n : setattr(self, 'role_kind', n.get_enum_value(planner_user_role_kind.PlannerUserRoleKind)),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def role_kind(self,) -> Optional[planner_user_role_kind.PlannerUserRoleKind]:
        """
        Gets the roleKind property value. The roleKind property
        Returns: Optional[planner_user_role_kind.PlannerUserRoleKind]
        """
        return self._role_kind
    
    @role_kind.setter
    def role_kind(self,value: Optional[planner_user_role_kind.PlannerUserRoleKind] = None) -> None:
        """
        Sets the roleKind property value. The roleKind property
        Args:
            value: Value to set for the role_kind property.
        """
        self._role_kind = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("roleKind", self.role_kind)
        writer.write_additional_data_value(self.additional_data)
    


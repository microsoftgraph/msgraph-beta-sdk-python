from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_container_type, planner_shared_with_container

class PlannerPlanContainer(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerPlanContainer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier of the resource that contains the plan. Optional.
        self._container_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type of the resource that contains the plan. For supported types, see the previous table. Possible values are: group, unknownFutureValue, roster, and project. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: roster, project. Optional.
        self._type: Optional[planner_container_type.PlannerContainerType] = None
        # The full canonical URL of the container. Optional.
        self._url: Optional[str] = None
    
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
    
    @property
    def container_id(self,) -> Optional[str]:
        """
        Gets the containerId property value. The identifier of the resource that contains the plan. Optional.
        Returns: Optional[str]
        """
        return self._container_id
    
    @container_id.setter
    def container_id(self,value: Optional[str] = None) -> None:
        """
        Sets the containerId property value. The identifier of the resource that contains the plan. Optional.
        Args:
            value: Value to set for the container_id property.
        """
        self._container_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.plannerSharedWithContainer":
                from . import planner_shared_with_container

                return planner_shared_with_container.PlannerSharedWithContainer()
        return PlannerPlanContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_container_type, planner_shared_with_container

        fields: Dict[str, Callable[[Any], None]] = {
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(planner_container_type.PlannerContainerType)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("containerId", self.container_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[planner_container_type.PlannerContainerType]:
        """
        Gets the type property value. The type of the resource that contains the plan. For supported types, see the previous table. Possible values are: group, unknownFutureValue, roster, and project. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: roster, project. Optional.
        Returns: Optional[planner_container_type.PlannerContainerType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[planner_container_type.PlannerContainerType] = None) -> None:
        """
        Sets the type property value. The type of the resource that contains the plan. For supported types, see the previous table. Possible values are: group, unknownFutureValue, roster, and project. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: roster, project. Optional.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. The full canonical URL of the container. Optional.
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. The full canonical URL of the container. Optional.
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    


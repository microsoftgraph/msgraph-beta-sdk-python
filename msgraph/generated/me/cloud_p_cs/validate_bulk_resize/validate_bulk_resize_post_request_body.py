from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ValidateBulkResizePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new validateBulkResizePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cloudPcIds property
        self._cloud_pc_ids: Optional[List[str]] = None
        # The targetServicePlanId property
        self._target_service_plan_id: Optional[str] = None
    
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
    def cloud_pc_ids(self,) -> Optional[List[str]]:
        """
        Gets the cloudPcIds property value. The cloudPcIds property
        Returns: Optional[List[str]]
        """
        return self._cloud_pc_ids
    
    @cloud_pc_ids.setter
    def cloud_pc_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the cloudPcIds property value. The cloudPcIds property
        Args:
            value: Value to set for the cloud_pc_ids property.
        """
        self._cloud_pc_ids = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateBulkResizePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidateBulkResizePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidateBulkResizePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPcIds": lambda n : setattr(self, 'cloud_pc_ids', n.get_collection_of_primitive_values(str)),
            "targetServicePlanId": lambda n : setattr(self, 'target_service_plan_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("cloudPcIds", self.cloud_pc_ids)
        writer.write_str_value("targetServicePlanId", self.target_service_plan_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target_service_plan_id(self,) -> Optional[str]:
        """
        Gets the targetServicePlanId property value. The targetServicePlanId property
        Returns: Optional[str]
        """
        return self._target_service_plan_id
    
    @target_service_plan_id.setter
    def target_service_plan_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetServicePlanId property value. The targetServicePlanId property
        Args:
            value: Value to set for the target_service_plan_id property.
        """
        self._target_service_plan_id = value
    


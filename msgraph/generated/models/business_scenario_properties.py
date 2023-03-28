from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class BusinessScenarioProperties(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new businessScenarioProperties and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier for the bucketDefinition configured in the plannerPlanConfiguration for the scenario. The task will be placed in the corresponding plannerBucket in the target plan. Required.
        self._external_bucket_id: Optional[str] = None
        # The identifier for the context of the task. Context is an application controlled value, and tasks can be queried by their externalContextId. Optional.
        self._external_context_id: Optional[str] = None
        # Application-specific identifier for the task. Every task for the same scenario must have a unique identifier specified for this property. Required.
        self._external_object_id: Optional[str] = None
        # Application-specific version of the task. Optional.
        self._external_object_version: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The URL to the application-specific experience for this task. Optional.
        self._web_url: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenarioProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessScenarioProperties()
    
    @property
    def external_bucket_id(self,) -> Optional[str]:
        """
        Gets the externalBucketId property value. The identifier for the bucketDefinition configured in the plannerPlanConfiguration for the scenario. The task will be placed in the corresponding plannerBucket in the target plan. Required.
        Returns: Optional[str]
        """
        return self._external_bucket_id
    
    @external_bucket_id.setter
    def external_bucket_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalBucketId property value. The identifier for the bucketDefinition configured in the plannerPlanConfiguration for the scenario. The task will be placed in the corresponding plannerBucket in the target plan. Required.
        Args:
            value: Value to set for the external_bucket_id property.
        """
        self._external_bucket_id = value
    
    @property
    def external_context_id(self,) -> Optional[str]:
        """
        Gets the externalContextId property value. The identifier for the context of the task. Context is an application controlled value, and tasks can be queried by their externalContextId. Optional.
        Returns: Optional[str]
        """
        return self._external_context_id
    
    @external_context_id.setter
    def external_context_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalContextId property value. The identifier for the context of the task. Context is an application controlled value, and tasks can be queried by their externalContextId. Optional.
        Args:
            value: Value to set for the external_context_id property.
        """
        self._external_context_id = value
    
    @property
    def external_object_id(self,) -> Optional[str]:
        """
        Gets the externalObjectId property value. Application-specific identifier for the task. Every task for the same scenario must have a unique identifier specified for this property. Required.
        Returns: Optional[str]
        """
        return self._external_object_id
    
    @external_object_id.setter
    def external_object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalObjectId property value. Application-specific identifier for the task. Every task for the same scenario must have a unique identifier specified for this property. Required.
        Args:
            value: Value to set for the external_object_id property.
        """
        self._external_object_id = value
    
    @property
    def external_object_version(self,) -> Optional[str]:
        """
        Gets the externalObjectVersion property value. Application-specific version of the task. Optional.
        Returns: Optional[str]
        """
        return self._external_object_version
    
    @external_object_version.setter
    def external_object_version(self,value: Optional[str] = None) -> None:
        """
        Sets the externalObjectVersion property value. Application-specific version of the task. Optional.
        Args:
            value: Value to set for the external_object_version property.
        """
        self._external_object_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "externalBucketId": lambda n : setattr(self, 'external_bucket_id', n.get_str_value()),
            "externalContextId": lambda n : setattr(self, 'external_context_id', n.get_str_value()),
            "externalObjectId": lambda n : setattr(self, 'external_object_id', n.get_str_value()),
            "externalObjectVersion": lambda n : setattr(self, 'external_object_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("externalBucketId", self.external_bucket_id)
        writer.write_str_value("externalContextId", self.external_context_id)
        writer.write_str_value("externalObjectId", self.external_object_id)
        writer.write_str_value("externalObjectVersion", self.external_object_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The URL to the application-specific experience for this task. Optional.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The URL to the application-specific experience for this task. Optional.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    


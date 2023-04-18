from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import service_provisioning_resource_error, service_provisioning_xml_error

class ServiceProvisioningError(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new serviceProvisioningError and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The isResolved property
        self._is_resolved: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The serviceInstance property
        self._service_instance: Optional[str] = None
    
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
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceProvisioningError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceProvisioningError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.serviceProvisioningResourceError":
                from . import service_provisioning_resource_error

                return service_provisioning_resource_error.ServiceProvisioningResourceError()
            if mapping_value == "#microsoft.graph.serviceProvisioningXmlError":
                from . import service_provisioning_xml_error

                return service_provisioning_xml_error.ServiceProvisioningXmlError()
        return ServiceProvisioningError()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import service_provisioning_resource_error, service_provisioning_xml_error

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isResolved": lambda n : setattr(self, 'is_resolved', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceInstance": lambda n : setattr(self, 'service_instance', n.get_str_value()),
        }
        return fields
    
    @property
    def is_resolved(self,) -> Optional[bool]:
        """
        Gets the isResolved property value. The isResolved property
        Returns: Optional[bool]
        """
        return self._is_resolved
    
    @is_resolved.setter
    def is_resolved(self,value: Optional[bool] = None) -> None:
        """
        Sets the isResolved property value. The isResolved property
        Args:
            value: Value to set for the is_resolved property.
        """
        self._is_resolved = value
    
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isResolved", self.is_resolved)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serviceInstance", self.service_instance)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_instance(self,) -> Optional[str]:
        """
        Gets the serviceInstance property value. The serviceInstance property
        Returns: Optional[str]
        """
        return self._service_instance
    
    @service_instance.setter
    def service_instance(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceInstance property value. The serviceInstance property
        Args:
            value: Value to set for the service_instance property.
        """
        self._service_instance = value
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import rbac_application, rbac_application_multiple, unified_rbac_application

class RoleManagement(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new RoleManagement and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cloudPC property
        self._cloud_p_c: Optional[rbac_application_multiple.RbacApplicationMultiple] = None
        # The RbacApplication for Device Management
        self._device_management: Optional[rbac_application_multiple.RbacApplicationMultiple] = None
        # The directory property
        self._directory: Optional[rbac_application.RbacApplication] = None
        # The RbacApplication for Entitlement Management
        self._entitlement_management: Optional[rbac_application.RbacApplication] = None
        # The exchange property
        self._exchange: Optional[unified_rbac_application.UnifiedRbacApplication] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def cloud_p_c(self,) -> Optional[rbac_application_multiple.RbacApplicationMultiple]:
        """
        Gets the cloudPC property value. The cloudPC property
        Returns: Optional[rbac_application_multiple.RbacApplicationMultiple]
        """
        return self._cloud_p_c
    
    @cloud_p_c.setter
    def cloud_p_c(self,value: Optional[rbac_application_multiple.RbacApplicationMultiple] = None) -> None:
        """
        Sets the cloudPC property value. The cloudPC property
        Args:
            value: Value to set for the cloud_p_c property.
        """
        self._cloud_p_c = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleManagement()
    
    @property
    def device_management(self,) -> Optional[rbac_application_multiple.RbacApplicationMultiple]:
        """
        Gets the deviceManagement property value. The RbacApplication for Device Management
        Returns: Optional[rbac_application_multiple.RbacApplicationMultiple]
        """
        return self._device_management
    
    @device_management.setter
    def device_management(self,value: Optional[rbac_application_multiple.RbacApplicationMultiple] = None) -> None:
        """
        Sets the deviceManagement property value. The RbacApplication for Device Management
        Args:
            value: Value to set for the device_management property.
        """
        self._device_management = value
    
    @property
    def directory(self,) -> Optional[rbac_application.RbacApplication]:
        """
        Gets the directory property value. The directory property
        Returns: Optional[rbac_application.RbacApplication]
        """
        return self._directory
    
    @directory.setter
    def directory(self,value: Optional[rbac_application.RbacApplication] = None) -> None:
        """
        Sets the directory property value. The directory property
        Args:
            value: Value to set for the directory property.
        """
        self._directory = value
    
    @property
    def entitlement_management(self,) -> Optional[rbac_application.RbacApplication]:
        """
        Gets the entitlementManagement property value. The RbacApplication for Entitlement Management
        Returns: Optional[rbac_application.RbacApplication]
        """
        return self._entitlement_management
    
    @entitlement_management.setter
    def entitlement_management(self,value: Optional[rbac_application.RbacApplication] = None) -> None:
        """
        Sets the entitlementManagement property value. The RbacApplication for Entitlement Management
        Args:
            value: Value to set for the entitlement_management property.
        """
        self._entitlement_management = value
    
    @property
    def exchange(self,) -> Optional[unified_rbac_application.UnifiedRbacApplication]:
        """
        Gets the exchange property value. The exchange property
        Returns: Optional[unified_rbac_application.UnifiedRbacApplication]
        """
        return self._exchange
    
    @exchange.setter
    def exchange(self,value: Optional[unified_rbac_application.UnifiedRbacApplication] = None) -> None:
        """
        Sets the exchange property value. The exchange property
        Args:
            value: Value to set for the exchange property.
        """
        self._exchange = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import rbac_application, rbac_application_multiple, unified_rbac_application

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPC": lambda n : setattr(self, 'cloud_p_c', n.get_object_value(rbac_application_multiple.RbacApplicationMultiple)),
            "deviceManagement": lambda n : setattr(self, 'device_management', n.get_object_value(rbac_application_multiple.RbacApplicationMultiple)),
            "directory": lambda n : setattr(self, 'directory', n.get_object_value(rbac_application.RbacApplication)),
            "entitlementManagement": lambda n : setattr(self, 'entitlement_management', n.get_object_value(rbac_application.RbacApplication)),
            "exchange": lambda n : setattr(self, 'exchange', n.get_object_value(unified_rbac_application.UnifiedRbacApplication)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("cloudPC", self.cloud_p_c)
        writer.write_object_value("deviceManagement", self.device_management)
        writer.write_object_value("directory", self.directory)
        writer.write_object_value("entitlementManagement", self.entitlement_management)
        writer.write_object_value("exchange", self.exchange)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


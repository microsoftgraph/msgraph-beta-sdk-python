from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_troubleshooting_error_resource = lazy_import('msgraph.generated.models.device_management_troubleshooting_error_resource')

class DeviceManagementTroubleshootingErrorDetails(AdditionalDataHolder, Parsable):
    """
    Object containing detailed information about the error and its remediation.
    """
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
        Instantiates a new deviceManagementTroubleshootingErrorDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Not yet documented
        self._context: Optional[str] = None
        # Not yet documented
        self._failure: Optional[str] = None
        # The detailed description of what went wrong.
        self._failure_details: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The detailed description of how to remediate this issue.
        self._remediation: Optional[str] = None
        # Links to helpful documentation about this failure.
        self._resources: Optional[List[device_management_troubleshooting_error_resource.DeviceManagementTroubleshootingErrorResource]] = None
    
    @property
    def context(self,) -> Optional[str]:
        """
        Gets the context property value. Not yet documented
        Returns: Optional[str]
        """
        return self._context
    
    @context.setter
    def context(self,value: Optional[str] = None) -> None:
        """
        Sets the context property value. Not yet documented
        Args:
            value: Value to set for the context property.
        """
        self._context = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementTroubleshootingErrorDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTroubleshootingErrorDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementTroubleshootingErrorDetails()
    
    @property
    def failure(self,) -> Optional[str]:
        """
        Gets the failure property value. Not yet documented
        Returns: Optional[str]
        """
        return self._failure
    
    @failure.setter
    def failure(self,value: Optional[str] = None) -> None:
        """
        Sets the failure property value. Not yet documented
        Args:
            value: Value to set for the failure property.
        """
        self._failure = value
    
    @property
    def failure_details(self,) -> Optional[str]:
        """
        Gets the failureDetails property value. The detailed description of what went wrong.
        Returns: Optional[str]
        """
        return self._failure_details
    
    @failure_details.setter
    def failure_details(self,value: Optional[str] = None) -> None:
        """
        Sets the failureDetails property value. The detailed description of what went wrong.
        Args:
            value: Value to set for the failureDetails property.
        """
        self._failure_details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "context": lambda n : setattr(self, 'context', n.get_str_value()),
            "failure": lambda n : setattr(self, 'failure', n.get_str_value()),
            "failure_details": lambda n : setattr(self, 'failure_details', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediation": lambda n : setattr(self, 'remediation', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(device_management_troubleshooting_error_resource.DeviceManagementTroubleshootingErrorResource)),
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
    
    @property
    def remediation(self,) -> Optional[str]:
        """
        Gets the remediation property value. The detailed description of how to remediate this issue.
        Returns: Optional[str]
        """
        return self._remediation
    
    @remediation.setter
    def remediation(self,value: Optional[str] = None) -> None:
        """
        Sets the remediation property value. The detailed description of how to remediate this issue.
        Args:
            value: Value to set for the remediation property.
        """
        self._remediation = value
    
    @property
    def resources(self,) -> Optional[List[device_management_troubleshooting_error_resource.DeviceManagementTroubleshootingErrorResource]]:
        """
        Gets the resources property value. Links to helpful documentation about this failure.
        Returns: Optional[List[device_management_troubleshooting_error_resource.DeviceManagementTroubleshootingErrorResource]]
        """
        return self._resources
    
    @resources.setter
    def resources(self,value: Optional[List[device_management_troubleshooting_error_resource.DeviceManagementTroubleshootingErrorResource]] = None) -> None:
        """
        Sets the resources property value. Links to helpful documentation about this failure.
        Args:
            value: Value to set for the resources property.
        """
        self._resources = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("context", self.context)
        writer.write_str_value("failure", self.failure)
        writer.write_str_value("failureDetails", self.failure_details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("remediation", self.remediation)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_additional_data_value(self.additional_data)
    


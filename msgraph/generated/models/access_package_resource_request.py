from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_resource = lazy_import('msgraph.generated.models.access_package_resource')
access_package_subject = lazy_import('msgraph.generated.models.access_package_subject')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageResourceRequest(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def access_package_resource(self,) -> Optional[access_package_resource.AccessPackageResource]:
        """
        Gets the accessPackageResource property value. The accessPackageResource property
        Returns: Optional[access_package_resource.AccessPackageResource]
        """
        return self._access_package_resource
    
    @access_package_resource.setter
    def access_package_resource(self,value: Optional[access_package_resource.AccessPackageResource] = None) -> None:
        """
        Sets the accessPackageResource property value. The accessPackageResource property
        Args:
            value: Value to set for the accessPackageResource property.
        """
        self._access_package_resource = value
    
    @property
    def catalog_id(self,) -> Optional[str]:
        """
        Gets the catalogId property value. The unique ID of the access package catalog.
        Returns: Optional[str]
        """
        return self._catalog_id
    
    @catalog_id.setter
    def catalog_id(self,value: Optional[str] = None) -> None:
        """
        Sets the catalogId property value. The unique ID of the access package catalog.
        Args:
            value: Value to set for the catalogId property.
        """
        self._catalog_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageResourceRequest and sets the default values.
        """
        super().__init__()
        # The accessPackageResource property
        self._access_package_resource: Optional[access_package_resource.AccessPackageResource] = None
        # The unique ID of the access package catalog.
        self._catalog_id: Optional[str] = None
        # The executeImmediately property
        self._execute_immediately: Optional[bool] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._expiration_date_time: Optional[datetime] = None
        # If set, does not add the resource.
        self._is_validation_only: Optional[bool] = None
        # The requestor's justification for adding or removing the resource.
        self._justification: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. Nullable. Supports $expand.
        self._requestor: Optional[access_package_subject.AccessPackageSubject] = None
        # The outcome of whether the service was able to add the resource to the catalog.  The value is Delivered if the resource was added or removed. Read-Only.
        self._request_state: Optional[str] = None
        # The requestStatus property
        self._request_status: Optional[str] = None
        # Use AdminAdd to add a resource, if the caller is an administrator or resource owner, AdminUpdate to update a resource, or AdminRemove to remove a resource.
        self._request_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageResourceRequest()
    
    @property
    def execute_immediately(self,) -> Optional[bool]:
        """
        Gets the executeImmediately property value. The executeImmediately property
        Returns: Optional[bool]
        """
        return self._execute_immediately
    
    @execute_immediately.setter
    def execute_immediately(self,value: Optional[bool] = None) -> None:
        """
        Sets the executeImmediately property value. The executeImmediately property
        Args:
            value: Value to set for the executeImmediately property.
        """
        self._execute_immediately = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package_resource": lambda n : setattr(self, 'access_package_resource', n.get_object_value(access_package_resource.AccessPackageResource)),
            "catalog_id": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "execute_immediately": lambda n : setattr(self, 'execute_immediately', n.get_bool_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "is_validation_only": lambda n : setattr(self, 'is_validation_only', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "requestor": lambda n : setattr(self, 'requestor', n.get_object_value(access_package_subject.AccessPackageSubject)),
            "request_state": lambda n : setattr(self, 'request_state', n.get_str_value()),
            "request_status": lambda n : setattr(self, 'request_status', n.get_str_value()),
            "request_type": lambda n : setattr(self, 'request_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_validation_only(self,) -> Optional[bool]:
        """
        Gets the isValidationOnly property value. If set, does not add the resource.
        Returns: Optional[bool]
        """
        return self._is_validation_only
    
    @is_validation_only.setter
    def is_validation_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the isValidationOnly property value. If set, does not add the resource.
        Args:
            value: Value to set for the isValidationOnly property.
        """
        self._is_validation_only = value
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The requestor's justification for adding or removing the resource.
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The requestor's justification for adding or removing the resource.
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def requestor(self,) -> Optional[access_package_subject.AccessPackageSubject]:
        """
        Gets the requestor property value. Read-only. Nullable. Supports $expand.
        Returns: Optional[access_package_subject.AccessPackageSubject]
        """
        return self._requestor
    
    @requestor.setter
    def requestor(self,value: Optional[access_package_subject.AccessPackageSubject] = None) -> None:
        """
        Sets the requestor property value. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the requestor property.
        """
        self._requestor = value
    
    @property
    def request_state(self,) -> Optional[str]:
        """
        Gets the requestState property value. The outcome of whether the service was able to add the resource to the catalog.  The value is Delivered if the resource was added or removed. Read-Only.
        Returns: Optional[str]
        """
        return self._request_state
    
    @request_state.setter
    def request_state(self,value: Optional[str] = None) -> None:
        """
        Sets the requestState property value. The outcome of whether the service was able to add the resource to the catalog.  The value is Delivered if the resource was added or removed. Read-Only.
        Args:
            value: Value to set for the requestState property.
        """
        self._request_state = value
    
    @property
    def request_status(self,) -> Optional[str]:
        """
        Gets the requestStatus property value. The requestStatus property
        Returns: Optional[str]
        """
        return self._request_status
    
    @request_status.setter
    def request_status(self,value: Optional[str] = None) -> None:
        """
        Sets the requestStatus property value. The requestStatus property
        Args:
            value: Value to set for the requestStatus property.
        """
        self._request_status = value
    
    @property
    def request_type(self,) -> Optional[str]:
        """
        Gets the requestType property value. Use AdminAdd to add a resource, if the caller is an administrator or resource owner, AdminUpdate to update a resource, or AdminRemove to remove a resource.
        Returns: Optional[str]
        """
        return self._request_type
    
    @request_type.setter
    def request_type(self,value: Optional[str] = None) -> None:
        """
        Sets the requestType property value. Use AdminAdd to add a resource, if the caller is an administrator or resource owner, AdminUpdate to update a resource, or AdminRemove to remove a resource.
        Args:
            value: Value to set for the requestType property.
        """
        self._request_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accessPackageResource", self.access_package_resource)
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_bool_value("executeImmediately", self.execute_immediately)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_bool_value("isValidationOnly", self.is_validation_only)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("requestor", self.requestor)
        writer.write_str_value("requestState", self.request_state)
        writer.write_str_value("requestStatus", self.request_status)
        writer.write_str_value("requestType", self.request_type)
    

